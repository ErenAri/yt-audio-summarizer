import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")  # .env veya Streamlit secret ile alınacak


def summarize_text(text, model="gpt-3.5-turbo"):
    prompt = f"Aşağıdaki metni kısa ve öz şekilde özetle:\n\n{text}"

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=500
    )

    summary = response['choices'][0]['message']['content']
    
    with open("summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)

    print("Özet oluşturuldu ve summary.txt dosyasına kaydedildi.")
    return summary
