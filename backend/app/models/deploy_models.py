The FastAPI application in the question contains the necessary Pydantic model for the request body. The model `HerokuDeploymentRequest` is used to validate the data coming in the request body. The model has two fields `app_name` and `source_blob_url`, both of which are of type string.

Here is the Pydantic model for request:

```python
from pydantic import BaseModel

class HerokuDeploymentRequest(BaseModel):
    app_name: str
    source_blob_url: str
```

For the response model, it seems that the endpoint always returns a dictionary with a single key `status` and a string message. A Pydantic model for this response could look like this:

```python
class DeploymentResponse(BaseModel):
    status: str
```

If you want to use this response model in your endpoint, you can declare it in the function signature as follows:

```python
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import httpx
import logging
from typing import Optional
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.security.api_key import APIKeyQuery, APIKeyHeader, APIKeyCookie, APIKey
from starlette.status import HTTP_403_FORBIDDEN

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

API_KEY = "1234567abcdef"
API_KEY_NAME = "api_key"
api_key_query = APIKeyQuery(name=API_KEY_NAME, auto_error=False)

class HerokuDeploymentRequest(BaseModel):
    app_name: str
    source_blob_url: str

class DeploymentResponse(BaseModel):
    status: str

async def get_api_key(
    api_key_query: str = Depends(api_key_query),
    token: str = Depends(oauth2_scheme),
):
    if api_key_query == API_KEY:
        return token
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )

@app.post("/deploy/", response_model=DeploymentResponse)
async def deploy(heroku_deployment: HerokuDeploymentRequest, api_key: APIKey = Depends(get_api_key)):
    """
    Trigger a new deployment on Heroku.

    This will take the source code from the given URL and deploy it to the specified Heroku app.
    """
    response = await httpx.post(
        f"https://api.heroku.com/apps/{heroku_deployment.app_name}/builds",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/vnd.heroku+json; version=3",
        },
        json={
            "source_blob": {
                "url": heroku_deployment.source_blob_url,
                "version": "v1",
            },
        },
    )

    if response.status_code != 201:
        logging.error(f"Failed to trigger deployment: {response.text}")
        raise HTTPException(status_code=500, detail="Failed to trigger deployment")

    return {"status": "Deployment triggered"}
```

This will ensure that FastAPI validates the response data and generates an appropriate OpenAPI schema.