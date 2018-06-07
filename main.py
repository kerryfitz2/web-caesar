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
        <form action = "/" method = "post">
            <label for = "rot">Rotate by:</label>
            <input id = "rotation" type = "text" name = "rot" />
            <textarea id = "text_area" type = "text" name = "text" placeholder = "test..."></textarea>
            <input type = "submit" value = "Submit Query"/>
        </form>
    </body>
<html>
"""

@app.route("/")
def index():
    return form

app.run()