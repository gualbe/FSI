import sqlite3
from db_conn2 import sql_connection

con = sql_connection("mydatabase.db")

cur = con.cursor()

try:
    cur.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")
    con.commit()
    print("The table is created.")
except sqlite3.OperationalError:
    print("The table already exists.")

con.close()
