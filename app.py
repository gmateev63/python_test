from fastapi import FastAPI
import os
import json
import sqlite3
import duckdb

app = FastAPI()
con = duckdb.connect("mydb.duckdb")

con.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER,
        name VARCHAR,
        age INTEGER
    )
""")

con.execute("""
    INSERT INTO users VALUES
        (1, 'Alice', 30),
        (2, 'Bob', 25),
        (3, 'Charlie', 35)
""")

@app.get("/users")
def get_users(min_age: int = 0):
    """Return all users older than min_age"""
    df = con.execute(
        "SELECT * FROM users WHERE age > ?", [min_age]
    ).fetchdf()
    return df.to_dict(orient="records")

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
def duck():
    #result = duckdb.sql("SELECT name,id FROM 'flights.csv'").fetchall()    
    
    
    #duckdb.read_csv("example.csv")                # read a CSV file into a Relation
    #duckdb.read_parid	name
    #duckdb.read_json("example.json")              # read a JSON file into a Relation
    #duckdb.sql("SELECT * FROM 'example.csv'")     # directly query a CSV file
    #duckdb.sql("SELECT * FROM 'example.parquet'") # directly query a Parquet file
    #duckdb.sql("SELECT * FROM 'example.json'")    # directly query a JSON file
    
    con = duckdb.connect("duck1.duckdb")
    cursor = con.cursor()
    sql = "select 40"

    try:
        res = cursor.execute(sql)
        print(res)
    except:
        l.logger.error("Error: Bad database. Check the file signal_translator.db")
        return {"result": "err"}
    #stres = cursor.fetchone()
    
    
    return {"result": res}
    #return {"result": "temp"}
