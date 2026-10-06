from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
from pathlib import Path

app = Flask(__name__)
DB_PATH = Path("data") / "students.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                roll_no TEXT NOT NULL UNIQUE,
                course TEXT NOT NULL
            )
        """)
        conn.commit()

@app.route("/")
def index():
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        students = conn.execute("SELECT * FROM students ORDER BY id DESC").fetchall()
    return render_template("index.html", students=students)

@app.route("/add", methods=["POST"])
def add_student():
    name = request.form["name"].strip()
    roll_no = request.form["roll_no"].strip()
    course = request.form["course"].strip()

    if not name or not roll_no or not course:
        return redirect(url_for("index"))

    try:
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute(
                "INSERT INTO students (name, roll_no, course) VALUES (?, ?, ?)",
                (name, roll_no, course),
            )
            conn.commit()
    except sqlite3.IntegrityError:
        pass

    return redirect(url_for("index"))

@app.route("/delete/<int:student_id>", methods=["POST"])
def delete_student(student_id):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
    return redirect(url_for("index"))

@app.route("/health")
def health():
    return jsonify(status="healthy", application="Student Management System")

init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
