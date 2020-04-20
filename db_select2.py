import sqlite3
from db_conn2 import sql_connection

con = sql_connection("mydatabase.db")

cur = con.cursor()

# Method 1
cur.execute('SELECT id, name FROM employees WHERE salary > 800.0')
res = [row for row in cur.fetchall()]
print(res)

# Method 2
cur.execute('SELECT id, name, salary FROM employees')
res = [(row[0], row[1]) for row in cur.fetchall() if row[2] > 800.0]
print(res)

con.close()
