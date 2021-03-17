import sqlite3

con = sqlite3.connect("mydatabase.db")

cur = con.cursor()

con.close()
