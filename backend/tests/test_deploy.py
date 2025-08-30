Here are the unit tests for the given FastAPI endpoint. We will use pytest and FastAPI's TestClient for making requests to the application in a test environment.

```python
from fastapi.testclient import TestClient
from main import app, HerokuDeploymentRequest, get_api_key
import pytest
import httpx
from starlette.status import HTTP_403_FORBIDDEN, HTTP_500_INTERNAL_SERVER_ERROR
from fastapi import HTTPException

client = TestClient(app)

def test_deploy_success():
    """
    Test case for successful deployment
    """
    with httpx.MockTransport() as mock:
        def mock_request(request):
            assert request.url.path == "/apps/test-app/builds"
            assert request.method == "POST"
            return httpx.Response(201, json={"status": "Deployment triggered"})

        mock.add_route("/apps/test-app/builds", mock_request)

        response = client.post("/deploy/", 
                                json={"app_name": "test-app", 
                                      "source_blob_url": "https://example.com/source.tar.gz"},
                                headers={"api_key": "1234567abcdef", 
                                         "Authorization": "Bearer test-token"})
        
        assert response.status_code == 201
        assert response.json() == {"status": "Deployment triggered"}


def test_deploy_failure():
    """
    Test case for deployment failure
    """
    with httpx.MockTransport() as mock:
        def mock_request(request):
            assert request.url.path == "/apps/test-app/builds"
            assert request.method == "POST"
            return httpx.Response(500, text="Deployment failed")

        mock.add_route("/apps/test-app/builds", mock_request)

        response = client.post("/deploy/", 
                                json={"app_name": "test-app", 
                                      "source_blob_url": "https://example.com/source.tar.gz"},
                                headers={"api_key": "1234567abcdef", 
                                         "Authorization": "Bearer test-token"})
        
        assert response.status_code == HTTP_500_INTERNAL_SERVER_ERROR


def test_get_api_key_unauthorized():
    """
    Test case for unauthorized request
    """
    with pytest.raises(HTTPException):
        get_api_key(api_key_query="wrong_key", token="test-token")


def test_validation_error():
    """
    Test case for validation error
    """
    response = client.post("/deploy/", 
                            json={"app_name": "", 
                                  "source_blob_url": "https://example.com/source.tar.gz"},
                            headers={"api_key": "1234567abcdef", 
                                     "Authorization": "Bearer test-token"})
    
    assert response.status_code == 422
    assert "field required" in response.text
```

These tests cover the success and error cases, data validation, and edge cases for the `/deploy/` endpoint. They use a mock HTTP client to simulate responses from the Heroku API. The `test_deploy_success` and `test_deploy_failure` tests simulate successful and failed deployments, respectively. The `test_get_api_key_unauthorized` test checks the behavior when the API key is incorrect, and the `test_validation_error` test checks the validation of the request body.