from fastapi import FastAPI
import os
import json
import sqlite3
import duckdb

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from Render!"}

@app.get("/files")    
def list_files():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    #return {"files":json.dumps(files)}
    return files

@app.get("/db")    
def db():
    conn = sqlite3.connect("signal_translator.db")
    cursor = conn.cursor()
    sql = "select min(pk) from history"

    try:
        res = cursor.execute(sql)
    except:
        l.logger.error("Error: Bad database. Check the file signal_translator.db")
        return {"result": "err"}
    stres = cursor.fetchone()
       
    return {"sql": sql,"result": stres[0]}

@app.get("/duckdb")    
def duckdb():

    #duckdb.read_csv("example.csv")                # read a CSV file into a Relation
    #duckdb.read_parquet("example.parquet")        # read a Parquet file into a Relation
    #duckdb.read_json("example.json")              # read a JSON file into a Relation

    duckdb.sql("SELECT * FROM 'example.csv'")     # directly query a CSV file
    #duckdb.sql("SELECT * FROM 'example.parquet'") # directly query a Parquet file
    #duckdb.sql("SELECT * FROM 'example.json'")    # directly query a JSON file

    
    conn = sqlite3.connect("signal_translator.db")
    cursor = conn.cursor()
    sql = "select message from history where pk=580"

    try:
        res = cursor.execute(sql)
    except:
        l.logger.error("Error: Bad database. Check the file signal_translator.db")
        return {"result": "err"}
    stres = cursor.fetchone()
       
    return {"sql": sql,"result": stres[0]}
