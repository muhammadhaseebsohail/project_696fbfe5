To generate an API endpoint for the task, we'll need one POST endpoint to create a task, and Pydantic models to validate the data. For the service layer, we'll have a simple in-memory "database" to store the tasks. Lastly, we'll need to include an authentication dependency to ensure only authorized users can create tasks.

Here are the necessary parts:

1. The complete endpoint code with all imports:

```python
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from pydantic import BaseModel
from uuid import uuid4
from typing import Dict, Optional
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# In-memory "database"
tasks_db = {}

class Task(BaseModel):
    name: str
    requirements: List[str]

class TaskOut(BaseModel):
    id: str
    name: str
    requirements: List[str]

def get_current_user(token: str = Depends(oauth2_scheme)):
    # This function should implement actual user authentication
    # For this example, we'll just check if token equals 'valid'
    if token != 'valid':
        raise HTTPException(status_code=401, detail="Invalid token")
    return token

@app.post("/task", response_model=TaskOut)
def create_task(task: Task, user: str = Depends(get_current_user)):
    """
    Create a new task
    """
    task_id = str(uuid4())
    tasks_db[task_id] = {"name": task.name, "requirements": task.requirements}
    return {"id": task_id, "name": task.name, "requirements": task.requirements}
```

2. Pydantic models for request/response:

The models are included in the code above: `Task` for the request, and `TaskOut` for the response.

3. Any necessary service layer code:

In this example, the service layer code is minimal. The `create_task` function simply writes the task to the in-memory "database". In a real application, you would want to replace this with calls to a real database or other persistent storage.

Note: This code includes an example of how to use FastAPI's dependency injection system to handle authentication. In a real application, the `get_current_user` function should be replaced with actual code that validates the user's token and retrieves their user information.