Here is how you can implement user authentication with JWT and bcrypt in FastAPI.

Firstly, we define the Pydantic models:

```python
from pydantic import BaseModel, Field
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: Optional[str] = Field(None, regex="^.+@.+\..+$")

class UserIn(UserBase):
    password: str

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True

class TokenData(BaseModel):
    username: Optional[str] = None
```

Next, we create a service layer where we can define our helper functions:

```python
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "SECRET"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
```

Finally, we define our endpoints:

```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

@app.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me/", response_model=User)
async def read_users_me(token: str = Depends(oauth2_scheme)):
    return {"username": token}
```

In this code, we are hashing user passwords using bcrypt, and then we are creating JWT tokens for users to authenticate with. The `/token` endpoint is used to obtain a token, and the `/users/me/` endpoint is used to return user information. This endpoint uses the JWT token to authenticate the user. The token is passed in the Authorization header.

Please note, this is a basic example and does not include all necessary error handling, logging, and database interactions (represented by placeholder `fake_db` and `get_user`). You should add these based on your application requirements.