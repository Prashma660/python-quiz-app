from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)

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

    quiz_duration = 300

    return render_template(
        "quiz.html",
        questions=questions,
        remaining_seconds=quiz_duration
    )


@app.route("/submit", methods=["POST"])
def submit():

    score = 0

    username = request.form.get("username", "Unknown")

    for i, q in enumerate(questions):

        selected = request.form.get(f"q{i}", "")

        if selected == q["answer"]:
            score += 1

    with open("scores.csv", "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([username, score])

    return redirect("/leaderboard")


@app.route("/leaderboard")
def leaderboard():

    scores = []

    try:

        with open("scores.csv", "r") as file:

            reader = csv.reader(file)

            for row in reader:

                if len(row) == 2:
                    scores.append(row)

    except:
        pass

    scores.sort(key=lambda x: int(x[1]), reverse=True)

    return render_template(
        "leaderboard.html",
        scores=scores
    )


if __name__ == "__main__":
    app.run(debug=True)