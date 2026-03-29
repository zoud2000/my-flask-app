import sqlite3

conn=sqlite3.connect("users.db")
cursor=conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name Text,
        age Integer,
        city Text     
    )
   """)

conn.commit()
conn.close()
print("数据库创建成功")

