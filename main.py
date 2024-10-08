from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel) :
	# If no value the field will be required
	text: str
	is_done: bool = False

items = []

@app.get("/api")
def root():
	return {"API working"}

# post item with item = string param
@app.post("/api/items")
def add_item( item: Item):
	items.append(item)
	return items


# get all items in a list with limit = int param
@app.get("/api/items", response_model=List[Item])
def get_items(limit: int = 10):
	if len(items) > 0:
		return items[0:limit]
	else:
		return HTTPException(status_code=404, detail="No items found")
		
# get item with item_id = int param
@app.get("/api/items/{item_id}", response_model=Item)
def get_item(item_id: int):
	if item_id < len(items):
		return items[item_id]
	else:
		return HTTPException(status_code=404, detail="Item not found")
		

	