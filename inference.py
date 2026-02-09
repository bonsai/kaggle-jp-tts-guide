import os
import torch
import soundfile as sf
from style_bert_vits2.nlp import bert_models
from style_bert_vits2.constants import Languages
from style_bert_vits2.tts_model import TTSModel

def setup_jp_tts(model_dir):
    """
    日本語TTSモデルのセットアップ
    model_dir: モデルファイル(.safetensors, config.json, style_vectors.alps)が格納されているディレクトリ
    """
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    # BERTモデルのロード
    print("Loading BERT models...")
    bert_models.load_model(Languages.JP, "ku-nlp/deberta-v2-large-japanese-char-wwm")
    bert_models.load_tokenizer(Languages.JP, "ku-nlp/deberta-v2-large-japanese-char-wwm")
    
    # モデルファイルの特定
    model_path = None
    config_path = None
    style_path = None
    
    for f in os.listdir(model_dir):
        if f.endswith(".safetensors"):
            model_path = os.path.join(model_dir, f)
        elif f == "config.json":
            config_path = os.path.join(model_dir, f)
        elif f.endswith(".alps") or f == "style_vectors.p":
            style_path = os.path.join(model_dir, f)
            
    if not all([model_path, config_path, style_path]):
        raise FileNotFoundError("必要なモデルファイルが見つかりません。")
        
    print(f"Loading TTS model from {model_path}...")
    tts = TTSModel(
        model_path=model_path,
        config_path=config_path,
        style_vec_path=style_path,
        device=device
    )
    
    return tts

def generate_jp_speech(tts, text, output_path="output.wav"):
    """
    日本語音声を生成
    """
    print(f"Generating speech for: {text}")
    sr, audio = tts.infer(text=text)
    sf.write(output_path, audio, sr)
    print(f"Saved to {output_path}")

if __name__ == "__main__":
    # 使用例
    # tts = setup_jp_tts("./model_assets/my_model")
    # generate_jp_speech(tts, "こんにちは、世界！")
    pass
