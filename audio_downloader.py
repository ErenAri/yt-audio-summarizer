import yt_dlp
import os
import glob

def download_audio(youtube_url, output_path="audio.mp3"):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        before = set(glob.glob("*.mp3"))

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])

        after = set(glob.glob("*.mp3"))
        new_files = list(after - before)

        if new_files:
            newest = new_files[0]
            os.rename(newest, output_path)
            print(f"[✓] Dosya yeniden adlandırıldı: {newest} → {output_path}")
        else:
            print("[!] MP3 dosyası bulunamadı.")

        # 🎯 audio.mp3 dışındaki eski .mp3 dosyalarını sil
        for file in glob.glob("*.mp3"):
            if file != output_path:
                os.remove(file)
                print(f"[🗑️] Silindi: {file}")

    except Exception as e:
        print(f"[!] Hata oluştu: {e}")
