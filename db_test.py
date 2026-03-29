import sqlite3
conn=sqlite3.connect("users.db")
cursor=conn.cursor()

cursor.execute("""
    INSERT INTO Users(name,age,city)
    VALUES(?,?,?)
""",("David",50,"Dallas"))

conn.commit()

cursor.execute("SELECT * FROM users")
rows=cursor.fetchall()

for row in rows:
    print(f"id:{row[0]},name:{row[1]},age:{row[2]},city:{row[3]}")

conn.close