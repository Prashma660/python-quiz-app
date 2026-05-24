from flask import Flask, render_template, request, redirect
import csv
import os
from datetime import datetime

app = Flask(__name__)

# QUIZ TIMER SETTINGS
QUIZ_START = "2026-05-24 13:55:00"
QUIZ_END = "2026-05-24 13:59:00"

questions = [

    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    },

    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/* */", "--"],
        "answer": "#"
    },

    {
        "question": "Which data type stores True or False values?",
        "options": ["int", "float", "bool", "str"],
        "answer": "bool"
    },

    {
        "question": "Which function is used to display output in Python?",
        "options": ["echo()", "show()", "display()", "print()"],
        "answer": "print()"
    },

    {
        "question": "Which collection type is ordered and changeable?",
        "options": ["Set", "Tuple", "Dictionary", "List"],
        "answer": "List"
    }

]

# Create scores.csv if not exists
if not os.path.exists("scores.csv"):
    with open("scores.csv", "w", newline="") as file:
        pass


@app.route("/")
def home():

    current_time = datetime.now()

    start_time = datetime.strptime(QUIZ_START, "%Y-%m-%d %H:%M:%S")
    end_time = datetime.strptime(QUIZ_END, "%Y-%m-%d %H:%M:%S")

    # BEFORE QUIZ START
    if current_time < start_time:
        return render_template(
            "waiting.html",
            start_time=QUIZ_START
        )

    # AFTER QUIZ END
    if current_time > end_time:
        return "<h1>Quiz Time Over</h1>"

    # QUIZ ACTIVE
    remaining_seconds = int((end_time - current_time).total_seconds())

    return render_template(
        "quiz.html",
        questions=questions,
        remaining_seconds=remaining_seconds
    )


@app.route("/submit", methods=["POST"])
def submit():

    current_time = datetime.now()

    end_time = datetime.strptime(QUIZ_END, "%Y-%m-%d %H:%M:%S")

    # Prevent late submissions
    if current_time > end_time:
        return "<h1>Submission Time Over</h1>"

    score = 0

    username = request.form["username"]

    for i, q in enumerate(questions):

        selected = request.form.get(f"q{i}")

        if selected == q["answer"]:
            score += 1

    with open("scores.csv", "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([username, score])

    return redirect("/leaderboard")


@app.route("/leaderboard")
def leaderboard():

    scores = []

    with open("scores.csv", "r") as file:

        reader = csv.reader(file)

        for row in reader:

            if len(row) == 2:
                scores.append(row)

    scores.sort(key=lambda x: int(x[1]), reverse=True)

    return render_template(
        "leaderboard.html",
        scores=scores
    )


if __name__ == "__main__":
    app.run(debug=True)