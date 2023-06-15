import sqlite3
# connect to the database
con = sqlite3.connect('data.db')
# print("here is a data base exist!")
cur = con.cursor()
# cur.execute('CREATE TABLE Product (p_id INTEGER PRIMARY KEY AUTOINCREMENT, p_name TEXT NOT NULL, price REAL, quantity INTEGER)')
# print("create table")

#insert data
cur.execute("INSERT INTO Product(p_name, price, quantity) VALUES('CAD', 200, 20)")
cur.execute("INSERT INTO Product(p_name, price, quantity) VALUES('car', 400, 100)")
cur.execute("INSERT INTO Product(p_name, price, quantity) VALUES('moo', 100, 1)")
print("data insert")
#commit and close
con.commit()
con.close()
