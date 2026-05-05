from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)

# Connect to Supabase PostgreSQL
conn = psycopg2.connect(
    "postgresql://postgres:Javan,,%4012@db.xdpuxfbjlbbnjtmkssjl.supabase.co:5432/postgres"
)

@app.route('/')
def home():
    cursor = conn.cursor()
    cursor.execute("SELECT name, email FROM users")
    rows = cursor.fetchall()
    return render_template("index.html", users=rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))