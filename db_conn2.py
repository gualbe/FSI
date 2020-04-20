import sqlite3
from sqlite3 import Error

def sql_connection(filename = ":memory:"):
    try:
        con = sqlite3.connect(filename)
        print("Connection is established to", filename)
    except Error:
        print(Error)
        con = None
    finally:
        return con

if __name__ == "main":
    con = sql_connection("mydatabase.db")
    con.close()