The necessary Pydantic models have already been included in your provided code. Here they are for quick reference:

```python
# Pydantic models
class TodoBase(BaseModel):
    title: str
    description: str

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    id: str

    class Config:
        orm_mode = True
```

1. `TodoBase`: This is the base model which includes the fields `title` and `description` that are common to both the creation and display of a todo item.

2. `TodoCreate`: This model is used when creating a new todo item. It inherits from `TodoBase`.

3. `Todo`: This is the model used for displaying a todo item. It includes an `id` field in addition to the fields from `TodoBase`.

The `Config` class inside the `Todo` model with `orm_mode = True` is necessary to allow the model to read data from MongoDB, because MongoDB returns data in a format that isn't automatically compatible with Pydantic models.

And here are again the necessary imports for your reference:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import status
```