"""GPT-SoVITS API client for Japanese voice cloning.

The model and API server are managed by the Kaggle notebook.
This file only sends inference requests and saves the returned WAV.
"""

import argparse
from pathlib import Path

import requests


def generate_jp_speech(
    text: str,
    ref_audio_path: str,
    prompt_text: str,
    output_path: str = "generated.wav",
    api_url: str = "http://127.0.0.1:9880",
) -> Path:
    """Generate Japanese speech using a reference recording and its transcript."""
    audio_path = Path(ref_audio_path)
    if not audio_path.is_file():
        raise FileNotFoundError(f"Reference audio not found: {audio_path}")
    if not text.strip():
        raise ValueError("Target text must not be empty.")
    if not prompt_text.strip():
        raise ValueError("Reference transcript must not be empty.")

    payload = {
        "text": text,
        "text_lang": "ja",
        "ref_audio_path": str(audio_path.resolve()),
        "prompt_text": prompt_text,
        "prompt_lang": "ja",
        "text_split_method": "cut5",
        "batch_size": 1,
        "media_type": "wav",
        "streaming_mode": False,
    }
    response = requests.post(
        f"{api_url.rstrip('/')}/tts",
        json=payload,
        timeout=600,
    )
    if response.status_code != 200 or not response.content.startswith(b"RIFF"):
        detail = response.text[:2000] if not response.content.startswith(b"RIFF") else ""
        raise RuntimeError(
            f"GPT-SoVITS API failed (HTTP {response.status_code}). {detail}"
        )

    destination = Path(output_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(response.content)
    return destination


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate Japanese speech through a running GPT-SoVITS API."
    )
    parser.add_argument("--text", required=True, help="Japanese text to speak")
    parser.add_argument("--ref-audio", required=True, help="Reference WAV path")
    parser.add_argument(
        "--prompt-text", required=True, help="Exact transcript of the reference WAV"
    )
    parser.add_argument("--output", default="generated.wav", help="Output WAV path")
    parser.add_argument("--api-url", default="http://127.0.0.1:9880")
    args = parser.parse_args()

    result = generate_jp_speech(
        text=args.text,
        ref_audio_path=args.ref_audio,
        prompt_text=args.prompt_text,
        output_path=args.output,
        api_url=args.api_url,
    )
    print(f"Saved generated speech: {result.resolve()}")


if __name__ == "__main__":
    main()
