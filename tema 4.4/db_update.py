import sqlite3
from db_conn2 import sql_connection

con = sql_connection("mydatabase.db")

cur = con.cursor()

cur.execute('UPDATE employees SET name = "Rogers" where id = 3')
con.commit()

con.close()
