from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))   

#1. Load the documennt
def load_document(filenames):
      combined = ""
      for filename in filenames:
            with open(filename, "r") as f:
                combined += f"\n\n--- {filename} ---\n"
                combined += f.read()
      return combined
    
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
document = load_document(["menu.txt","review.txt"])
print("Document loaded successfully! Ask me anything.")
print("-" *25)

while True:
    question = input("You: ").strip()  # strip removes extra spaces
    
    # Handle empty input
    if not question:
        print("AI: Please type a question.")
        continue
    
    #  quit if user type 'quit'
    if question.lower() == "quit":
        print("AI: Goodbye!")
        break
    
    # Handle very short input
    if len(question) < 3:
        print("AI: Please ask a complete question.")
        continue
    
    # Handles any wierd typo
    if not any(char.isalpha() for char in question):
        print("AI: Please ask a real question.")
        continue

    # Wrap API call in error handler
    try:
        answer = ask_about_doc(question, document)
        print(f"AI: {answer}")
    except Exception as e:
        print(f"AI: Sorry, something went wrong. Please try again.")
        print(f"Error: {e}")
    
    print("-" * 40)