import sqlite3
from db_conn2 import sql_connection

con = sql_connection("mydatabase.db")

cur = con.cursor()

try:
    employee = (1, 'John', 700, 'HR', 'Employee', '2017-01-04')
    cur.execute("INSERT INTO employees VALUES (?, ?, ?, ?, ?, ?)", employee)
    employee = (2, 'Marie', 1200, 'SALES', 'Manager', '2016-02-14')
    cur.execute("INSERT INTO employees VALUES (?, ?, ?, ?, ?, ?)", employee)
    employee = (3, 'Suzie', 900, 'HR', 'Manager', '2017-08-02')
    cur.execute("INSERT INTO employees VALUES (?, ?, ?, ?, ?, ?)", employee)
    con.commit()
    print("The registers were added.")
except sqlite3.IntegrityError as err:
    print("Error:", err)
    print("The registers were not added.")
except sqlite3.OperationalError as err:
    print("Error:", err)
    print("The registers were not added.")

con.close()
