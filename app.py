from audio_downloader import download_audio
from transcriber import transcribe_audio
from summarizer import summarize_text

def main():
    print("YouTube Linkini Girin:")
    url = input("> ")

    print("\n[1] Ses dosyası indiriliyor...")
    download_audio(url)

    print("\n[2] Ses metne dönüştürülüyor...")
    transcription = transcribe_audio("audio.mp3")

    print("\n[3] Metin özetleniyor...")
    summary = summarize_text(transcription)

    print("\nTüm adımlar tamamlandı!")
    print("\ntranscription.txt ve summary.txt dosyaları oluşturuldu.")

if __name__ == "__main__":
    main()
