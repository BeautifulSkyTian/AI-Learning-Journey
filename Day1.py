from fastapi import FastAPI

app = FastAPI()
@app.get("/") # Root directory 
async def root(): 
    return {"message": "This is the starting point of learning AI! 5/27/2026"}

@app.post("/chat") # This creates another route. Like a sub-page.
async def chat(message: str): 
    return {"response": f"You said: {message}"}

app2 = FastAPI() # When you create another FastAPI object, I guess FastAPI chooses the object that is first created. This is unnecessary. 
@app2.get("/")
async def something(): 
    return "wefwef"

#testing