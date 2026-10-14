# 自分の声を録る・覚える・使う

Colab Notebook を3ファイルに分け、録音から日本語音声生成までを順番に試します。

1. [声を録る — 001-record-voice.ipynb](001-record-voice.ipynb)：録音ファイルの読み込み、モノラル・32 kHz WAVへの変換、文字起こし
2. [声を覚える — 002-learn-voice.ipynb](002-learn-voice.ipynb)：GPT-SoVITSのセットアップ、参照音声の指定
3. [声を使う — 003-use-voice.ipynb](003-use-voice.ipynb)：API起動、日本語テキストからの音声生成

## 実行上の注意

- 3つの Notebook は同じ Colab ランタイムで順番に実行してください。
- 現状の「声を覚える」は追加学習ではなく、参照音声を使うゼロショット音声合成です。
- GPT-SoVITSの依存関係やモデル取得方法は更新されることがあり、Colab上での実行を保証するものではありません。
- 録音音声・文字起こし・生成音声は個人情報として扱い、公開データセットや共有Notebookに含めないでください。
