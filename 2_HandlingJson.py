from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Define a model using Pydantic

class User(BaseModel):
    id: int
    name: str
    email: str

#Post endpoint: accept a JSON body

@app.post("/users/") 
def creat_user(user: User):
    return {
        "message":"User created successfully",
        "user":user
    }      