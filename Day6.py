from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

#---------------------------------------
# Pydantic model
class Item(BaseModel): # Creating an object of a class that inherits the BaseModel class allows us to have create a Pydantic model object. 
    name: str
    description: str
    price: float = 0.0
    tax: float | None = None
# This class is actually very similar to a dataclass. The big difference is that a pydantic model stores data and validates it. 
# It also converts the string value from the client side to the type we specified in the backend.
# Using a dataclass would also work for our purposes, but since the client side gives the API string values, we would have to manually convert the strings to specified types. 

#---------------------------------------------
@app.get("/")
async def root(): 
    return {"message": "Today is day 6 of my AI learning journey. Today I will be working on request bodies and possibly integrating the gemini API."}

#-------------------------------------
# Request body ↓↓↓
# Using path parameters and query parameters in a request body is similar to doing it in a reponse body. 
# FastAPI recognizes that the path parameter is declared in the path. It recognizes that one of the parameters is a pydantic model object. And a normal parameter would be considered as a querye parameter. 
@app.post("/items/{item_id}")
async def create_item(item: Item, item_id: int, message: str): 
    return item

#-------------------------------
# Using model_dump()
# Since Item is a pydantic model object, we would need to convert it into a python dict which is what model_dump() does. 
@app.post("/items_v2")
async def create_itemV2(item: Item): 
    item_dict = item.model_dump() 
    if item.tax is not None: 
        item_dict.update({"price_with_tax": item.price + item.tax})
    print("This is backend.") # With this testing, it is clear that only things that interact with FastAPI shows up in the browser while backend stays in the backend. 
    return item_dict

#-----------------------------
# Using PUT path operation
# Put is responsible for updating values. Now here, there's really nothing to update and it looks almost just like a POST path operation. 
# Normally, we would have a DB and then values in the DB would be updated. 
@app.put("/update/{item_id}")
async def update_item(item_id: int, item: Item, q: int | None = None):
    result = {"item_id": item_id, **item.model_dump()} # ** is a python feature called dictionary unpacking. It basically expands the dictionary to include the new unpacked dictionary. 
    if q: 
        result.update({"q": q})
    return result