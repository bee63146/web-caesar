from flask import Flask, request, redirect
from caesar import rotate_string
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

page_header= """
<html>
    <head>
        <title>Web Caesar</title>
    </head>
    <body>
        <h1>Web Caesar</h1>
"""

add_form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
            p.error {{
                color: red;
            }}
        </style>
    </head>
    <body>
        <form action="/add" method="POST">
            <div>
                <label for="rot">Rotate by:</label>
                <input type="text" name="rot" value="0">
                <p class="error"></p>
            </div>
            <textarea type="text" name="text"></textarea>
            <br>
            <input type="submit">
        </form>
    </body>
</html>
"""
response = add_form + page_header

@app.route("/")
def index():
    return add_form.format(...)

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    if request.method == 'POST':

        return request(add_form + page_header)

app.run()
