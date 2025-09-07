from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#fake in-memory database
user_db = {}

#define a pydantic model
class User(BaseModel):
    id: int
    name: str
    email: str

@app.post("/users/")
def create_user(user:User):
    user_db[user.id]= user
    return{
        "message": "User created successfully",
        "user": user
    }

@app.get("/users/{user_id}")
def fetch_user(user_id:int):
    user = user_db.get(user_id)
    if not user:
        return {"error":"User not found"}
    return user

@app.put("/users/{user_id}")
def update_user(user_id:int,updated_user:User):
    if user_id not in user_db:
        return {"error":"User not found"}
    user_db[user_id] = updated_user
    return {
        "message":"User updated successfully",
        "user": updated_user
    }

# Delete
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id in user_db:
        del user_db[user_id]
        return {"message": "User deleted successfully"}
    return {"error": "User not found"}
