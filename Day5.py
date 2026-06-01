from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Zoo"}]

@app.get("/")
async def root(): 
    return {"message": "This is day 5 of our AI learning journey. Today I will be learning query parameters."}

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10): # This is query paramters which go like .../items/?skip=0&limit=10
    return fake_items_db[skip: skip + limit] # This is list slicing by the way. Don't forget like how I just did.
# Again, the way the process works is first the user enters the url which is a string. Then because we've declared the query parameters as int type, the url section responsible for the values of skip and limit would be 
# auto casted ot int type. This process is similar to the Enum class. 
# Query parameters are useful when say you are requesting information about users. /users/42 is an example of path parameter which requestes for #42 user. 
# Then /users?skip=20&limit=10 could be give me users but skip 20 and only return 10. 

#-------------------------------------------
@app.get("/items/{item_id}") # What's very interesting is when you want both path parameter and query parameter, fastapi can knows. We could do .../True?q=1
async def read_itemV2(item_id: bool, q: str | None = None): # You could declare an optional query parameter by setting its value to None. 
    if q: # Here's some funny stuff, apparently if I do .../yes?q=1
        return {"item_id": item_id, "q": q} # fastapi considers yes to be true somehow. 
    return {"item_id": item_id}

#--------------------------------------------
@app.get("/inventory/{add}/user/{user_id}")
async def inventory(add: bool, user_id: int, hour: str, min: str | None = None): 
    item = {1: 2}
    if add: 
        if min: 
            item.update({user_id: f"{hour}:{min}"}) # This runs just fine or you could expcitly cast this into a string type, then there would be no red lines. 
        else: 
            item.update({user_id: f"{hour}:00"})
    return item