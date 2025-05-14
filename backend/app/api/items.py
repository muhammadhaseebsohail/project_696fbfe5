To perform CRUD operations, we will first define our Pydantic models. The `ItemBase` model will be our base model and `ItemCreate` and `ItemUpdate` will inherit from it. The `Item` model will be used for reading data and includes the `id` field.
```python
from typing import Optional
from pydantic import BaseModel

class ItemBase(BaseModel):
    """Base model for items, includes name and description."""

    name: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    """Model for creating new items, inherits from ItemBase."""

    pass

class ItemUpdate(ItemBase):
    """Model for updating existing items, inherits from ItemBase."""

    pass

class Item(ItemBase):
    """Model for reading items data, includes id."""

    id: int
    class Config:
        orm_mode = True
```
Next, we will define our service layer that will handle the actual CRUD operations. In a real-world scenario, this would interact with a database.
```python
from typing import List, Optional
from fastapi import HTTPException
from .models import Item, ItemCreate, ItemUpdate

class ItemService:
    """Service layer for performing CRUD operations on items."""

    def __init__(self):
        self.items = []

    def get_all_items(self) -> List[Item]:
        return self.items

    def get_item(self, id: int) -> Item:
        item = next((item for item in self.items if item.id == id), None)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        return item

    def create_item(self, item: ItemCreate) -> Item:
        new_item = Item(id=len(self.items)+1, **item.dict())
        self.items.append(new_item)
        return new_item

    def update_item(self, id: int, item: ItemUpdate) -> Item:
        index = next((index for index, item in enumerate(self.items) if item.id == id), None)
        if index is None:
            raise HTTPException(status_code=404, detail="Item not found")
        updated_item = Item(id=id, **item.dict())
        self.items[index] = updated_item
        return updated_item

    def delete_item(self, id: int) -> None:
        index = next((index for index, item in enumerate(self.items) if item.id == id), None)
        if index is None:
            raise HTTPException(status_code=404, detail="Item not found")
        self.items.pop(index)
```
Finally, we will define our API endpoints. These will use the ItemService to perform operations and return results.
```python
from fastapi import FastAPI
from .models import Item, ItemCreate, ItemUpdate
from .service import ItemService

app = FastAPI()
service = ItemService()

@app.get("/items/", response_model=List[Item])
async def read_items():
    """Endpoint to get all items."""
    return service.get_all_items()

@app.get("/items/{id}", response_model=Item)
async def read_item(id: int):
    """Endpoint to get an item by its id."""
    return service.get_item(id)

@app.post("/items/", response_model=Item)
async def create_item(item: ItemCreate):
    """Endpoint to create a new item."""
    return service.create_item(item)

@app.put("/items/{id}", response_model=Item)
async def update_item(id: int, item: ItemUpdate):
    """Endpoint to update an existing item."""
    return service.update_item(id, item)

@app.delete("/items/{id}")
async def delete_item(id: int):
    """Endpoint to delete an existing item."""
    service.delete_item(id)
    return {"message": "Item deleted successfully."}
```
The above code provides a simple implementation of CRUD operations using FastAPI and Pydantic. In a real-world application, the service layer would interact with a database and you would have to consider things like transactions and error handling for database operations.