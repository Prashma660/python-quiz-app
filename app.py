from flask import Flask, render_template, request

app = Flask(__name__)

questions = [

# ---------------- EASY ---------------- #

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
    "question": "Which function is used to display output in Python?",
    "options": ["echo()", "display()", "print()", "show()"],
    "answer": "print()"
},

{
    "question": "Which data type stores True or False values?",
    "options": ["int", "bool", "str", "float"],
    "answer": "bool"
},

{
    "question": "What is the index of the first element in a list?",
    "options": ["0", "1", "-1", "2"],
    "answer": "0"
},

# ---------------- MEDIUM ---------------- #

{
    "question": "Which method adds an element to the end of a list?",
    "options": ["insert()", "append()", "add()", "push()"],
    "answer": "append()"
},

{
    "question": "Which operator is used for exponentiation?",
    "options": ["^", "**", "//", "%"],
    "answer": "**"
},

{
    "question": "Which loop is used when the number of iterations is unknown?",
    "options": ["for", "while", "loop", "repeat"],
    "answer": "while"
},

{
    "question": "Which function converts a string into an integer?",
    "options": ["str()", "float()", "int()", "bool()"],
    "answer": "int()"
},

{
    "question": "Which keyword is used to handle exceptions?",
    "options": ["error", "catch", "try", "except"],
    "answer": "try"
},

# ---------------- APPLICATION LEVEL ---------------- #

{
    "question": "Which data structure is best for storing unique values?",
    "options": ["List", "Tuple", "Set", "Dictionary"],
    "answer": "Set"
},

{
    "question": "Which method removes all elements from a list?",
    "options": ["remove()", "delete()", "clear()", "pop()"],
    "answer": "clear()"
},

{
    "question": "What will len('Python') return?",
    "options": ["5", "6", "7", "Error"],
    "answer": "6"
},

{
    "question": "Which keyword is used to stop a loop immediately?",
    "options": ["stop", "break", "continue", "exit"],
    "answer": "break"
},

{
    "question": "Which collection stores key-value pairs?",
    "options": ["Set", "Tuple", "Dictionary", "List"],
    "answer": "Dictionary"
},

# ---------------- TOUGH ---------------- #

{
    "question": "What is the output of: type([1,2,3])?",
    "options": ["tuple", "set", "list", "dict"],
    "answer": "list"
},

{
    "question": "Which keyword is used to create a class in Python?",
    "options": ["object", "class", "define", "struct"],
    "answer": "class"
},

{
    "question": "What is the output of: 5 // 2 ?",
    "options": ["2.5", "2", "3", "1"],
    "answer": "2"
},

{
    "question": "Which method converts text to lowercase?",
    "options": ["lower()", "small()", "down()", "case()"],
    "answer": "lower()"
},

{
    "question": "What is the output of: bool(0) ?",
    "options": ["True", "False", "0", "Error"],
    "answer": "False"
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