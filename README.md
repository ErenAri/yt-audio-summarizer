# 🎧 YouTube Audio Summarizer with AI

Bu proje, kullanıcıdan bir YouTube video linki alır, videonun sesini indirir, Whisper ile transkribe eder ve GPT-3.5 ile özet çıkarır. Streamlit tabanlı web arayüzü ile kolay kullanım sunar.

## 🔧 Özellikler
- 🎥 YouTube videosundan ses indirme (yt-dlp)
- 🧠 Whisper ile otomatik konuşma-metin dönüşümü
- 📝 OpenAI GPT ile özetleme
- 🌐 Streamlit arayüzü
- ✅ Gereksiz MP3 dosyalarını otomatik temizleme

## 🚀 Canlı Demo
👉 [Buraya tıkla](https://yt-audio-summarizer.streamlit.app/)

## 📦 Kurulum

```bash
git clone https://github.com/kullaniciadi/yt-audio-summarizer.git
cd yt-audio-summarizer
pip install -r requirements.txt
streamlit run web_app.py
