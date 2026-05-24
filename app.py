from flask import Flask, render_template, request

app = Flask(__name__)

questions = [

    {
        "question": "What is the correct extension of Python file?",
        "options": [".py", ".java", ".html", ".cpp"],
        "answer": ".py"
    },

    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "define", "def", "fun"],
        "answer": "def"
    },

    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/* */", "--"],
        "answer": "#"
    },

    {
        "question": "Which data type is used to store text?",
        "options": ["int", "float", "str", "bool"],
        "answer": "str"
    },

    {
        "question": "What is the output of 2 + 3?",
        "options": ["5", "6", "23", "4"],
        "answer": "5"
    },

    {
        "question": "Which function is used to display output?",
        "options": ["show()", "display()", "print()", "output()"],
        "answer": "print()"
    },

    {
        "question": "Which loop is used to repeat code multiple times?",
        "options": ["if", "for", "def", "break"],
        "answer": "for"
    },

    {
        "question": "Which keyword is used for conditional statements?",
        "options": ["loop", "if", "repeat", "switch"],
        "answer": "if"
    },

    {
        "question": "Which operator is used for multiplication?",
        "options": ["+", "-", "*", "/"],
        "answer": "*"
    },

    {
        "question": "Which function is used to take user input?",
        "options": ["get()", "input()", "scan()", "enter()"],
        "answer": "input()"
    },

    {
        "question": "Which bracket is used for lists?",
        "options": ["()", "{}", "[]", "<>"],
        "answer": "[]"
    },

    {
        "question": "Which keyword is used to exit a loop?",
        "options": ["stop", "end", "break", "exit"],
        "answer": "break"
    },

    {
        "question": "Which of these is a Python boolean value?",
        "options": ["Yes", "True", "1", "On"],
        "answer": "True"
    },

    {
        "question": "What is the output type of 5 / 2 in Python?",
        "options": ["int", "float", "str", "bool"],
        "answer": "float"
    },

    {
        "question": "Which keyword is used to create a class?",
        "options": ["object", "class", "define", "struct"],
        "answer": "class"
    },

    {
        "question": "Which collection stores key-value pairs?",
        "options": ["list", "tuple", "dictionary", "set"],
        "answer": "dictionary"
    },

    {
        "question": "Which function gives the length of a list?",
        "options": ["count()", "size()", "len()", "length()"],
        "answer": "len()"
    },

    {
        "question": "Which keyword is used to import modules?",
        "options": ["include", "using", "import", "load"],
        "answer": "import"
    },

    {
        "question": "Which of these is immutable?",
        "options": ["list", "dictionary", "set", "tuple"],
        "answer": "tuple"
    },

    {
        "question": "Which keyword is used to handle exceptions?",
        "options": ["error", "try", "catch", "handle"],
        "answer": "try"
    }

]

@app.route('/')
def home():
    return render_template('quiz.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0

    for i, q in enumerate(questions):
        selected = request.form.get(f'q{i}')

        if selected == q['answer']:
            score += 1

    return f"<h1>Your Score: {score}/{len(questions)}</h1>"

if __name__ == '__main__':
    app.run(debug=True)