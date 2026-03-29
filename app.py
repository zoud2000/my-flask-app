from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    conn = get_db()
    users = conn.execute("SELECT * FROM users").fetchall()
    conn.close()
    return render_template("home.html", users=users)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method=="POST":
        name = request.form["name"]
        age = request.form["age"]
        city = request.form["city"]
        conn = get_db()
        conn.execute("INSERT INTO users (name, age, city) VALUES (?, ?, ?)",
                    (name, age, city))
        conn.commit()
        conn.close()
        return home()
    else:
        return "这是添加用户的页面，请填写表单提交！"        

if __name__ == "__main__":
    app.run(debug=True)