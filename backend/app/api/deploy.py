Deployment tasks are usually not performed through API endpoints, but rather through CI/CD pipelines (Continuous Integration/Continuous Deployment). They are automated processes that are set up on the server-side. 

However, in some cases, you might want to trigger the deployment process from a backend application. This might be the case if you have a management application that controls several aspects of your CI/CD pipeline.

In this case, you can create an endpoint that triggers the deployment process. This will involve calling the Heroku API to create a new deployment. 

Here is a sample FastAPI endpoint that could potentially be used to trigger a Heroku deployment:

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

@app.post("/deploy/")
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

This FastAPI application includes one POST endpoint, /deploy/. This endpoint requires a JSON body with the Heroku app name and the URL of the source code blob. The source code blob is a tarball of your source code, hosted somewhere accessible via a URL.

The endpoint uses HTTP Basic Authentication to authenticate with the Heroku API. This requires a Heroku API key, which you can generate from your Heroku account.

The request to the Heroku API is made using httpx, an async HTTP client for Python. If the request is successful, the endpoint returns a 201 Created response. If the request fails for any reason, the endpoint logs the error and returns a 500 Internal Server Error response.

Also, this endpoint uses both OAuth2 and API key for dual authentication. Please replace "1234567abcdef" with your actual API key.

Please note that this is a basic example and a real-world application would need more sophisticated error handling and security measures.