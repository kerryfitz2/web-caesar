from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action = "/encrypt" method = "post">
            <label for = "rot">Rotate by:</label>
            <input id = "rot" type = "text" name = "rot" />
            <textarea id = "text" type = "text" name = "text" placeholder = "test..."></textarea>
            <input type = "submit" value = "Submit Query"/>
        </form>
    </body>
<html>
"""

@app.route("/")
def index():
    return form

@app.route("/encrypt", methods = ['POST'])
def encrypt():
    rot = int(request.form["rot"])
    text = request.form["text"]

    message = rotate_string(text, rot)

    return '<h1> Your new message is: "' + message + '."</h1>'

app.run()