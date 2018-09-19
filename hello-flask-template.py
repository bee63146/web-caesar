from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too
add form """
<!DOCTYPE html>

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
      <form>
    <form action="/add" method="post">
            <input type="text" type="textarea"/>
        <input name="rot" name="text"/>
    </form>
    </body>
</html>
"""
@app.route("/")
def index():
    
    return content



app.run()
