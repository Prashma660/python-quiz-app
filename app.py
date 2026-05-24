from flask import Flask, render_template, request

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


@app.route("/")
def home():

    return render_template(
        "quiz.html",
        questions=questions
    )


@app.route("/submit", methods=["POST"])
def submit():

    score = 0

    username = request.form.get("username")

    for i, q in enumerate(questions):

        selected = request.form.get(f"q{i}")

        if selected == q["answer"]:
            score += 1

    return render_template(
        "result.html",
        username=username,
        score=score,
        total=len(questions)
    )


if __name__ == "__main__":
    app.run(debug=True)