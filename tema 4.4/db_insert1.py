import sqlite3
from db_conn2 import sql_connection

con = sql_connection("mydatabase.db")

cur = con.cursor()

try:
    cur.execute("INSERT INTO employees VALUES (1, 'John', 700, 'HR', 'Manager', '2017-01-04')")
    con.commit()
    print("The register is added.")
except sqlite3.IntegrityError as err:
    print("Error:", err)
    print("The register was not added.")

con.close()
