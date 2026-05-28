from fastapi import FastAPI

app = FastAPI()
@app.get("/") # Root directory 
async def root(): 
    return "asdfasdfasdf"

@app.get("/Tianqi") # This creates another route. Like a sub-page.
async def me(): 
    return "This is Tianqi Pan right here."

app2 = FastAPI() # When you create another FastAPI object, I guess FastAPI chooses the object that is first created. This is unnecessary. 
@app2.get("/")
async def something(): 
    return "wefwef"

#testing