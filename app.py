from fastapi import FastAPI
import os
import json
import sqlite3
import duckdb
import redis

app = FastAPI()
con = duckdb.connect("mydb.duckdb")

con.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name VARCHAR,
        age INTEGER
    )
""")

con.execute("""
    INSERT INTO users VALUES
        (1, 'Alice', 30),
        (2, 'Bob', 25),
        (3, 'Charlie', 35)
    ON CONFLICT(id) DO NOTHING
""")

@app.get("/users")
def get_users(min_age: int = 0):
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
    rows = duckdb.query(f"""
        SELECT id, name 
        FROM 'flights.csv'
    """).fetchall()

@app.get("/redis")    
def get_redis():
    r = redis.from_url(os.environ['redis://red-d2e8qks9c44c73eib3jg:6379'])
    
    r.set('foo', 'bar')
    val = r.get('foo')
    print(val.decode())

    result = [{"id": r[0], "name": r[1]} for r in rows]
    return result
