from flask import Flask

app = Flask("My first web app")

@app.route("/")
def index():
    return "<p>If you are here on 19.12.2021, then I have birthday, yaaaaaaaaaaaaay</p>"