# 自分の声を録る・覚える・使う

自分の声を録音し、声の特徴をモデルに扱わせ、日本語テキストの読み上げに使うまでを、3段階で進めます。

## 1. 声を録る
[001-voice-data.ipynb](001-voice-data.ipynb)

- 静かな場所で自分の声を録音する
- 録音を読み込み、モノラル・32 kHz WAVに整える
- 録音内容と一致する文字起こしを保存する

## 2. 声を覚える
[002-voice-clone.ipynb](002-voice-clone.ipynb) のセットアップ・参照音声設定

- Kaggle の GPU 環境に GPT-SoVITS を準備する
- 録音と文字起こしを参照音声として指定する
- まずは追加学習なしで声の特徴を利用する

※ 現在の手順は、モデルを一から学習させるものではなく、参照音声を使うゼロショット音声合成です。

## 3. 声を使う
[002-voice-clone.ipynb](002-voice-clone.ipynb) の生成セルと [inference.py](inference.py)

- 読み上げたい日本語テキストを入力する
- 共通スクリプトで音声を生成する
- WAVを再生し、必要なら保存する

## 実行環境

- Kaggle Notebooks、GPU、Internet を有効化
- 001-voice-data.ipynb で作った WAV と文字起こしを Kaggle Input に追加
- 002-voice-clone.ipynb の入力パスを実際のパスに変更

## プライバシー

録音音声・文字起こし・生成音声は個人情報として扱い、公開データセットや公開 Notebook に含めないでください。Kaggle の共有設定と成果物の保存先も確認してください。

## 注意

GPT-SoVITS の依存関係・モデル取得方法・GPU対応状況は変わる場合があります。この Notebook は Kaggle 上での実行を保証するものではありません。
