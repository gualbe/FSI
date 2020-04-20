import sqlite3 as sql

class DB:
    def __init__ (self, filename = ":memory:"):
        try:
            self.conn = sql.connect(filename)
            self.cur = self.conn.cursor()
            print("Connection is established to", filename)
        except sql.Error as err:
            print(err)
            self.conn = None
    def create (self, create_table_sql):
        try:
            self.cur.execute(create_table_sql)
            self.conn.commit()
            print("The table is created.")
        except sql.OperationalError:
            print("The table already exists.")
        
    def insert (self, table, register):
        try:
            self.cur.execute("INSERT INTO " + table + " VALUES (?, ?, ?, ?, ?, ?)", register)
            self.conn.commit()
            print("The register was added.")
        except sql.IntegrityError as err:
            print("Error:", err)
            print("The register was not added.")
        except sql.OperationalError as err:
            print("Error:", err)
            print("The register was not added.")

    def select (self, select_sql):
        self.cur.execute(select_sql)
        res = [row for row in self.cur.fetchall()]
        return(res)
    
    def __del__ (self):
        self.conn.close()
