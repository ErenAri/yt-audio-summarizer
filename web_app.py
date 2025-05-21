import streamlit as st
from audio_downloader import download_audio
from transcriber import transcribe_audio
from summarizer import summarize_text
import os

st.title("🎧 YouTube Video Özetleyici (Yapay Zeka Destekli)")

url = st.text_input("YouTube video linkini girin:")

if st.button("Analizi Başlat"):
    if url.strip() == "":
        st.warning("Lütfen geçerli bir YouTube linki girin.")
    else:
        with st.spinner("1. Ses indiriliyor..."):
            download_audio(url)

        with st.spinner("2. Ses metne dönüştürülüyor..."):
            transcription = transcribe_audio("audio.mp3")

        st.subheader("🎙️ Transkripsiyon")
        st.text_area("Transkript:", transcription, height=300)

        with st.spinner("3. Metin özetleniyor..."):
            summary = summarize_text(transcription)

        st.subheader("🧠 Özet")
        st.write(summary)

        st.success("✅ İşlem tamamlandı!")
