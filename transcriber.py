import whisper

def transcribe_audio(audio_path="audio.mp3", model_size="base"):
    print(f"[i] Whisper modeli yükleniyor: {model_size}")
    model = whisper.load_model(model_size)

    print(f"[i] Transkripsiyon başlatılıyor: {audio_path}")
    result = model.transcribe(audio_path)

    text = result["text"]

    # Metni dosyaya kaydet
    with open("transcription.txt", "w", encoding="utf-8") as f:
        f.write(text)

    print("[✓] Transkripsiyon tamamlandı ve transcription.txt dosyasına kaydedildi.")
    return text
