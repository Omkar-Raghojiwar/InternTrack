from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

DATABASE = os.path.join(app.root_path, "database.db")


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS internships (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            role TEXT NOT NULL,
            location TEXT,
            application_date TEXT,
            deadline TEXT,
            status TEXT NOT NULL,
            interview_date TEXT,
            stipend TEXT,
            application_link TEXT,
            notes TEXT
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def index():
    conn = get_db_connection()

    internships = conn.execute(
        "SELECT * FROM internships ORDER BY id DESC"
    ).fetchall()

    total = conn.execute(
        "SELECT COUNT(*) FROM internships"
    ).fetchone()[0]

    applied = conn.execute(
        "SELECT COUNT(*) FROM internships WHERE status = 'Applied'"
    ).fetchone()[0]

    interview = conn.execute(
        "SELECT COUNT(*) FROM internships WHERE status = 'Interview'"
    ).fetchone()[0]

    selected = conn.execute(
        "SELECT COUNT(*) FROM internships WHERE status = 'Selected'"
    ).fetchone()[0]

    rejected = conn.execute(
        "SELECT COUNT(*) FROM internships WHERE status = 'Rejected'"
    ).fetchone()[0]

    conn.close()

    return render_template(
        "index.html",
        internships=internships,
        total=total,
        applied=applied,
        interview=interview,
        selected=selected,
        rejected=rejected
    )


@app.route("/add", methods=["GET", "POST"])
def add_internship():

    if request.method == "POST":

        company = request.form["company"]
        role = request.form["role"]
        location = request.form["location"]
        application_date = request.form["application_date"]
        deadline = request.form["deadline"]
        status = request.form["status"]
        interview_date = request.form["interview_date"]
        stipend = request.form["stipend"]
        application_link = request.form["application_link"]
        notes = request.form["notes"]

        conn = get_db_connection()

        conn.execute("""
            INSERT INTO internships
            (
                company,
                role,
                location,
                application_date,
                deadline,
                status,
                interview_date,
                stipend,
                application_link,
                notes
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            company,
            role,
            location,
            application_date,
            deadline,
            status,
            interview_date,
            stipend,
            application_link,
            notes
        ))

        conn.commit()
        conn.close()

        return redirect(url_for("index"))

    return render_template("add.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_internship(id):

    conn = get_db_connection()

    internship = conn.execute(
        "SELECT * FROM internships WHERE id = ?",
        (id,)
    ).fetchone()

    if request.method == "POST":

        company = request.form["company"]
        role = request.form["role"]
        location = request.form["location"]
        application_date = request.form["application_date"]
        deadline = request.form["deadline"]
        status = request.form["status"]
        interview_date = request.form["interview_date"]
        stipend = request.form["stipend"]
        application_link = request.form["application_link"]
        notes = request.form["notes"]

        conn.execute("""
            UPDATE internships
            SET company = ?,
                role = ?,
                location = ?,
                application_date = ?,
                deadline = ?,
                status = ?,
                interview_date = ?,
                stipend = ?,
                application_link = ?,
                notes = ?
            WHERE id = ?
        """, (
            company,
            role,
            location,
            application_date,
            deadline,
            status,
            interview_date,
            stipend,
            application_link,
            notes,
            id
        ))

        conn.commit()
        conn.close()

        return redirect(url_for("index"))

    conn.close()

    return render_template(
        "edit.html",
        internship=internship
    )


@app.route("/delete/<int:id>")
def delete_internship(id):

    conn = get_db_connection()

    conn.execute(
        "DELETE FROM internships WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)