# Kaggleで日本語特化型TTS (Style-Bert-VITS2) を動かすガイド

このガイドでは、Kaggle Notebook上で高品質な日本語音声合成モデル **Style-Bert-VITS2** を使用して音声を生成する手順を説明します。

## 1. 依存関係のインストール

Kaggle環境で必要なライブラリをインストールします。GPU（T4 x2 または P100）が有効であることを確認してください。

```python
# Style-Bert-VITS2本体のインストール
!pip install style-bert-vits2

# 日本語処理に必要な辞書のインストール
!pip install pyopenjtalk
```

## 2. BERTモデルと音声合成モデルの準備

日本語の自然なイントネーションを生成するために必要なBERTモデルと、デフォルトの音声モデルをロードします。

```python
from style_bert_vits2.nlp import bert_models
from style_bert_vits2.constants import Languages
from style_bert_vits2.tts_model import TTSModel
import torch

# デバイスの設定
device = "cuda" if torch.cuda.is_available() else "cpu"

# 日本語用BERTモデルのロード
bert_models.load_model(Languages.JP, "ku-nlp/deberta-v2-large-japanese-char-wwm")
bert_models.load_tokenizer(Languages.JP, "ku-nlp/deberta-v2-large-japanese-char-wwm")

# デフォルトの音声モデル（JVNVモデル等）をHugging Faceからダウンロードしてロード
# 初回実行時はダウンロードに少し時間がかかります
model_file = "model_assets/jvnv-F1-jp/jvnv-F1-jp_e160_s14000.safetensors"
config_file = "model_assets/jvnv-F1-jp/config.json"
style_file = "model_assets/jvnv-F1-jp/style_vectors.alps"

# モデルの初期化（JVNV-F1モデルを例に）
# 既存のモデルがない場合は、公式リポジトリのinitialize.pyと同様の処理を行うか、
# 手動でAssetsから取得したパスを指定します。
# ここではライブラリのデフォルト機能を利用したロード例を示します。

# ※注意: Kaggleでは /kaggle/working/ 以下のパスを使用します。
```

## 3. 音声生成の実行

テキストを入力して音声を生成し、ファイルに保存します。

```python
from style_bert_vits2.tts_model import TTSModel

# モデルのロード（パスは適宜調整してください）
# assets_root を指定して、モデルファイルを管理しやすくします。
tts = TTSModel(
    model_path="path/to/your/model.safetensors",
    config_path="path/to/your/config.json",
    style_vec_path="path/to/your/style_vectors.alps",
    device=device
)

text = "こんにちは。これはカグルで動かしている日本語の音声合成テストです。"

# 音声生成
sr, audio = tts.infer(text=text)

# 保存
import soundfile as sf
sf.write("output_jp.wav", audio, sr)
```

## 4. Notebookでの再生

```python
from IPython.display import Audio
Audio("output_jp.wav")
```

## 5. 便利なTips
- **感情制御**: Style-Bert-VITS2は「スタイル」を指定することで、喜び、悲しみ、怒りなどの感情を込めることができます。
- **話者変更**: 複数のモデルファイルを切り替えることで、異なるキャラクターの声で読み上げが可能です。
