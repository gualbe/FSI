import sqlite3
from db_conn2 import sql_connection

con = sql_connection("mydatabase.db")

cur = con.cursor()

cur.execute('SELECT id, name FROM employees WHERE salary > 800.0')
rows = cur.fetchall()

for row in rows:
    print(row)

con.close()
