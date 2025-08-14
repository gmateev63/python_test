from fastapi import FastAPI
import os
import json

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from Render (/)!"}
    
@app.get("/path1")
def home1():
    return {"message": "Hello from Render (/path1)!"}

@app.get("/files")    
def list_files():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    #return {"files":json.dumps(files)}
    return files
