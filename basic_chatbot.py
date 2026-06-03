from fastapi import FastAPI
from google import genai
from dotenv import load_dotenv
from pydantic import BaseModel
import os
import json

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
#print(api_key)

client = genai.Client(api_key=api_key)

app = FastAPI()

class Chat(BaseModel): 
    personality: str
    message: str

@app.get("/")
async def root(): 
    return {"Introduction": "Welcome to using the basic version of Tianqi's chatbot."}

system_prompt = """
You are Tianqi's personal philosophical robot. 
Your job is to help people solve their confusions using Alfred Adler's mindset. 
You will be now named Solver. 
"""

personalities = {
    "wise man": "Patient. Speaks with profound knowledge and explains them in simple language. You can sense the kindness from him.", 
    "friend": "Speaks casually. Hangs out with you and supports you. You would feel relaxed and safe around him."
}

history = []

memory = []

@app.post("/gemini")
async def chatbot(message_json: Chat):
    user_message = message_json.message
    personality =  personalities[message_json.personality]
    
    for msg in history: 
        for key, value in msg.items(): 
            print(f"{key}: {value}\n")

    for msg in memory: 
        for key, value in msg.items(): 
            print(f"{key}: {value}\n")

    content = f"""
    
    Chat history: 
    {history}

    Memory: 
    {memory}
    
    System:
    {system_prompt}
    Your personality will be a {message_json.personality}: {personality}

    User: 
    {user_message}
    """

    try: 
        response = client.models.generate_content(
            model = "gemini-3.5-flash", 
            contents = content
        )

        history.append({"user": user_message})
        history.append({"System": response.text})
        memory.extend(json.loads(update_memory(user_message)))

        return {"speaker": "Solver", "response": response.text}
    except Exception as e: 
        return {"error": str(e)}

def update_memory(msg: str) -> str: 
    content = f"""
    Extract important long-term memories. 

    Message: {msg}

    Output JSON only. Make it structured like the following example:
    [{{"Name": "Tianqi"}}, 
    {{"Favourite food": "XiaoLongBao"}}]
    """

    try: 
        response = client.models.generate_content(
            model = "gemini-3.5-flash", 
            contents = content
        )

        return response.text or "[]"

    except Exception as e: 
        return "[]"
    
