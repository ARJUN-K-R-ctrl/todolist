# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory task storage
tasks = []

@app.route("/", methods=["GET", "POST"])
def index():
    global tasks
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append(task)
        return redirect(url_for("index"))
    return render_template("index.html", tasks=tasks)

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    global tasks
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
