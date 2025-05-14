Sure, here are comprehensive unit tests for the FastAPI endpoint mentioned above:

```python
from fastapi.testclient import TestClient
import pytest
from main import app, Task, tasks_db

client = TestClient(app)

def test_create_task_success():
    response = client.post("/task", 
                           json={"name": "task1", "requirements": ["requirement1", "requirement2"]},
                           headers={"Authorization": "Bearer valid"})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["name"] == "task1"
    assert data["requirements"] == ["requirement1", "requirement2"]
    assert data["id"] in tasks_db

def test_create_task_unauthorized():
    response = client.post("/task", 
                           json={"name": "task1", "requirements": ["requirement1", "requirement2"]},
                           headers={"Authorization": "Bearer invalid"})
    assert response.status_code == 401

def test_create_task_invalid_data():
    response = client.post("/task", 
                           json={"name": "task1", "requirements": "requirement1"},
                           headers={"Authorization": "Bearer valid"})
    assert response.status_code == 422

def test_create_task_no_data():
    response = client.post("/task", 
                           json={}, 
                           headers={"Authorization": "Bearer valid"})
    assert response.status_code == 422

def test_create_task_edge_case():
    # Edge case where task has no requirements
    response = client.post("/task", 
                           json={"name": "task1", "requirements": []},
                           headers={"Authorization": "Bearer valid"})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["name"] == "task1"
    assert data["requirements"] == []
    assert data["id"] in tasks_db
```

In this test suite, we're covering the following cases:

- `test_create_task_success`: A successful case where a task is created successfully with valid data and a valid token.
- `test_create_task_unauthorized`: An error case where an attempt is made to create a task with an invalid token.
- `test_create_task_invalid_data`: A data validation case where invalid data is sent (a string instead of a list for the `requirements` field).
- `test_create_task_no_data`: An edge case where no data is sent in the request body.
- `test_create_task_edge_case`: An edge case where a task is created with no requirements.

Each test makes a request to the `/task` endpoint and asserts that the response is as expected.