from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# This list is the AI's memory - starts empty
conversation_history = []

print("AI Chatbot is ready! Type 'quit' to exit.")
print("-" * 40)

while True:
    # Get input from user
    user_input = input("You: ")
    
    # Exit if user types quit
    if user_input.lower() == "quit":
        print("Goodbye!")
        break
    
    # Add user message to memory
    conversation_history.append({
        "role": "user",
        "content": user_input
    })
    
    # Send ENTIRE conversation history to AI
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation_history
    )
    
    # Extract AI's reply
    ai_reply = response.choices[0].message.content
    
    # Add AI's reply to memory too
    conversation_history.append({
        "role": "assistant",
        "content": ai_reply
    })
    
    print(f"AI: {ai_reply}")
    print("-" * 40)