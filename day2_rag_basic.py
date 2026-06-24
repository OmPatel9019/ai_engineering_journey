from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))   

#1. Load the documennt
def load_document(filename):
    with open(filename, "r") as f:
        return f.read()
    
# 2. Answsers the questions using doc as text
def ask_about_doc(question, doc_text):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"system",
                "content":f"""You are a document assistant. 
    
                STRICT RULES:
                1. Answer ONLY from the document below
                2. If the answer is not in the document, respond with exactly: 
                "This information is not in the document."
                3. Do NOT add any extra information
                4. Do NOT say "however" or give bonus information
                5. Keep answers short and direct

                DOCUMENT:
                {doc_text}"""
            },
            {
                "role":"user",
                "content": question
            }
        ]
    )
    return response.choices[0].message.content

#3. loads the document and start asking questions
document = load_document("company.txt")
print("Document loaded successfully! Ask me anything.")
print("-" *25)

while True:
    question = input("You: ")
    if question.lower() == "quit":
        break

    answer = ask_about_doc(question, document)
    print(f"AI: {answer}")
    print("-" *25)