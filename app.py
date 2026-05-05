from flask import Flask, render_template
import pyodbc

app = Flask(__name__)

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=MyWebsiteDB;"
    "Trusted_Connection=yes;"
)

@app.route('/')
def home():
    cursor = conn.cursor()
    cursor.execute("SELECT Name, Email FROM Users")
    rows = cursor.fetchall()
    return render_template("index.html", users=rows)

import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))