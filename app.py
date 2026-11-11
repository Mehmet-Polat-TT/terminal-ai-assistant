import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 1. Bota net ve sıkı kurallar koyuyoruz (System Prompt)
system_prompt = (
    "Sen arkadaş canlısı bir yapay zeka asistanısın. "
    "KURALLAR: Cevapların HER ZAMAN ultra kısa, net ve öz olmalı. "
    "Gerekmedikçe asla 2 cümleden uzun cevap verme. Gevezelik yapma."
)

sohbet_gecmisi = [
    {"role": "system", "content": system_prompt}
]

def mesaj_ekle(rol, icerik):
    sohbet_gecmisi.append({"role": rol, "content": icerik})

print("==========================================")
print("  CANLI AI CHATBOT (Kısa & Öz Modu)      ")
print("  Çıkmak için 'q' yazıp Enter'a bas.    ")
print("==========================================")

while True:
    kullanici_girdisi = input("\nSen: ")

    if kullanici_girdisi.lower() == 'q':
        print("\nChatbot kapatılıyor. İyi günler!")
        break

    mesaj_ekle("user", kullanici_girdisi)

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=sohbet_gecmisi,
            temperature=0.7,
            max_tokens=150  # Bota maksimum jeton/kelime sınırı koyuyoruz!
        )

        bot_cevabi = response.choices[0].message.content
        mesaj_ekle("assistant", bot_cevabi)

        print(f"\nBot: {bot_cevabi}")

    except Exception as e:
        print(f"\nBir hata oluştu: {e}")
