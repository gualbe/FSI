from db_class import DB

db = DB("employees.db")

db.create("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")

db.insert("employees", (1, 'John', 700, 'HR', 'Employee', '2017-01-04') )
db.insert("employees", (2, 'Marie', 1200, 'SALES', 'Manager', '2016-02-14') )
db.insert("employees", (3, 'Suzie', 900, 'HR', 'Manager', '2017-08-02') )

res = db.select('SELECT id, name FROM employees WHERE salary > 800.0')
print(res)
