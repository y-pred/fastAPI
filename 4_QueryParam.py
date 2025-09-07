    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel

    app = FastAPI()

    users_db = {}

    class User(BaseModel):
        id: int
        name: str
        email: str

    @app.post("/users/")
    def create_user(user:User):
        if user.id in users_db:
            raise HTTPException(status_code=400, detail="User already exists")
        users_db[user.id] = user
        return {
            "message" :" User created successfully",
            "user":user
        }

    # -------------------------
    # Search Users (Query Params)
    # -------------------------

    @app.get("/users/search/")
    def search_users(name:str = None, email: str = None):
        results = []
        for user in users_db.values():
            if (name and name.lower() in user.name.lower()) or (email and email.lower() in user.email.lower()):
                results.append(user)
        if not results:
            raise HTTPException(status_code=404, detail="No users found")
        return {
            "results": results
        }

    @app.get("/users/{user_id}")
    def get_user(user_id:int):
        if user_id in users_db:
            return users_db[user_id]
        raise HTTPException(status_code=404, detail="User not found")

    @app.put("/users/{user_id}")
    def update_user(user_id:int, updated_user:User):
        if user_id in users_db:
            users_db[user_id] = updated_user
            return {
                "message" : "Iser updated successfully",
                "user": "updated_user"
            }
        raise HTTPException(status_code=404, detail="User not found")
        
    @app.delete("/users/{user_id}")
    def delete_user(user_id: int):
        if user_id not in users_db:
            raise HTTPException(status_code=404, detail="User not found")
        del users_db[user_id]
        return {"message": "User deleted successfully"}

