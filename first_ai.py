from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response1 = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": "What is the real job role as an AI engineer? Respond in bullet"}
    ]
)

print(response1.choices[0].message.content)

print("\n===Exercise2: Sarcastic comment===")

response2 = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": "My name is Omie."},
        {"role": "assistant", "content": "Nice to meet you Omie! How can I help you today?"},
        {"role": "user", "content": "What is my name?"}
    ]
)
print(response2.choices[0].message.content)