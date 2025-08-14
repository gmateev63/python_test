from fastapi import FastAPI
import os
import json
import sqlite3

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

@app.get("/db")    
def db():
    conn = sqlite3.connect("signal_translator.db")
    cursor = conn.cursor()

    try:
        res = cursor.execute("select min(pk) from history")
    except:
        l.logger.error("Error: Bad database. Check the file signal_translator.db")
        return {"result": "err"}
    stres = cursor.fetchone()
       
    return {"result": stres[0]}