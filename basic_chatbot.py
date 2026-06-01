from fastapi import FastAPI
from google import genai
from dotenv import load_dotenv
from pydantic import BaseModel
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
#print(api_key)

client = genai.Client(api_key=api_key)

app = FastAPI()

class Chat(BaseModel): 
    identity: str
    description: str
    message: str

@app.get("/")
async def root(): 
    return {"Introduction": "Welcome to using the basic version of Tianqi's chatbot."}

@app.post("/gemini")
async def chatbot(message_json: Chat):
    chat_dict = message_json.model_dump()
    user_message = chat_dict["message"]

    try: 
        response = client.models.generate_content(
            model = "gemini-3.5-flash", 
            contents = user_message
        )

        return Chat(identity="Gemini", description="First response", message=response.text or "")
    
    except Exception as e: 
        return {"error": str(e)}

    # if response.text is None: 
    #     return {"error": "No reponse generated"}
    # return Chat(identity="Gemini", description="First response", message=response.text)


