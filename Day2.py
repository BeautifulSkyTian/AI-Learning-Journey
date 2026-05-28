from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root(): 
    return {"message": "Day2!!! 5/28/2026"}

@app.get("/items/{item_id}")
async def get_item(item_id: int): 
    return {"item_id": item_id}

@app.get("/square/{input}")
async def square(input: int): 
    return {"answer": f"{input*input}"}

#-------------------------------------------------------------
# If you ever try to redefine a path operation, the first one will always be used since the path matches first. A path operation is when you do @app.get("/something")
@app.get("/users/me")
async def read_user_me(): 
    return {"user id: " "the current user"}

@app.get("/users/{user_id}") # It is very important that we declare /users/me route before /user/{user_id}. If /user/{user_id} were to be declared first, then accessing /users/me would not call this actual route.     
async def read_user(user_id): 
    return {"user_id": user_id}