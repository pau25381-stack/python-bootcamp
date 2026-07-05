from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Index Page"


@app.route("/profile/")
def profile():
    return "This is a profile page"


app.run()
