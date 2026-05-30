from fastapi import FastAPI
from enum import Enum
from google import genai

app = FastAPI()

#---------------------------------------------------
# The whole point of creating an Enum is to have auto data validation and value restrictions. 
class ModelName(str, Enum): # You can see that we have "str, Enum" within the brackets. The purpose is to treat an Enum member of ModelName as a string. 
    gemini = "gemini1" # It is very important to know that Enum conversion happens by value, not by member identifier name.
    gpt = "gpt"

@app.get("/")
async def root(): 
    return {"message": "this is day 3 of the AI learning journey."}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName): # By declaring the parameter as a ModelName type, it tells fastapi that the value of model_name can only be the values that was declared in the Enum class. 
    if model_name is ModelName.gemini: # First model_name is supposed to be a string because URLs are strings. But then FastAPI converts the string into the corresponding Enum Member. 
        return {"model_name": model_name, "message": "Deep learning"} # In this if statement, say we input "gemini" which is a string, it is converted to the Enum member ModelName.gemini. 
    
    if model_name.value == "gpt": 
        return {"model_name": model_name, "message": "gpt is pretty useful"}
    
    return {"something": "hello"}
# Now you may ask why don't we just use if statements for data validation and value restrictions. You definitely can, but using an Enum enables automatic valdiation. 
# It allows better API documentation. We will see on FastAPI's /docs page about the exact allowed values. It also enables better type safety. It would guarantee the input to be one of our allowed values. It's also cleaner.

#-----------------------------------------------------
# Gemin API Learning
client = genai.Client()

response = client.models.generate_content(
    model = "gemini-3.5-flash", 
    contents = "Hi there! What is your name?"
)

print(response)