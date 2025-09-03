from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a simple endpoint that handles GET requests
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Define a second endpoint with a path parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/name/{name}")
def read_name(name: str):
    return {"message":f"Hello, {name}"}