# app.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from Render (/)!"}
    
    @app.get("/path1")
def home():
    return {"message": "Hello from Render (/path1)!"}
