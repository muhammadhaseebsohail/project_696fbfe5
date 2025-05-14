Sure, here is how you can write test cases for the FastAPI endpoint using pytest and FastAPI TestClient:

First, let's create a file test_main.py. The code is as follows:

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    # Success Case
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

    # Error Case
    response = client.get("/not_existent")
    assert response.status_code == 404

def test_read_root_validation():
    # Data Validation
    response = client.get("/?name=123")  # assuming name should be string
    assert response.status_code == 422

def test_read_root_edge_case():
    # Edge Case
    response = client.get("/?name=")  # Empty name
    assert response.status_code == 422
```

Here is what happens in the test code:

- First, we import `TestClient` from `fastapi.testclient` and `app` from `main.py` where we have our FastAPI application.

- We create a `client` using our FastAPI application.

- We then define four test functions, one for each case:

    - `test_read_root`: This tests the successful response from the root endpoint and an error response for a non-existent endpoint.

    - `test_read_root_validation`: This tests the data validation. We are passing a number as name when it should be a string (assuming name should be a string). It should return a 422 error code.

    - `test_read_root_edge_case`: This tests an edge case where the name is empty. It should also return a 422 error code.

To run the tests, we use pytest from the terminal:

```bash
pytest
```

Please note that the endpoint "/?name=" and the data validation test case are hypothetical. You would need to replace them with actual endpoints and validation logic from your application.