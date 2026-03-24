from flask import Flask, render_template, request
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    conn = mysql.connector.connect(
        host=os.environ.get("MYSQL_HOST"),
        user=os.environ.get("MYSQL_USER"),
        password=os.environ.get("MYSQL_PASSWORD"),
        database=os.environ.get("MYSQL_DATABASE")
    )
    return conn

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        delete_id = request.form.get("delete_id")
        completed_id = request.form.get("completed_id")
        task = request.form.get("task")

        conn = get_db_connection()
        cursor = conn.cursor()

        if delete_id:
            sql = "DELETE FROM tasks WHERE id = %s"
            cursor.execute(sql, (delete_id,))

        elif completed_id:
            sql = "UPDATE tasks SET completed = NOT completed WHERE id = %s"
            cursor.execute(sql, (completed_id,))

        elif task:
            sql = "INSERT INTO tasks (task) VALUES (%s)"
            cursor.execute(sql, (task,))

        conn.commit()
        cursor.close()
        conn.close()

    # フィルター取得
    filter_type = request.args.get("filter", "all")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # フィルター分岐
    if filter_type == "completed":
        cursor.execute("SELECT * FROM tasks WHERE completed = TRUE")
    elif filter_type == "incomplete":
        cursor.execute("SELECT * FROM tasks WHERE completed = FALSE")
    else:
        cursor.execute("SELECT * FROM tasks")

    tasks = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("index.html", tasks=tasks, filter_type=filter_type)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)