from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def landing():
    return render_template("introduction.html")


@app.route("/hobby/")
@app.route("/hobbies/")
def hobby():
    hobbies = ["Watching Movies", "Playing with my Kids", "Going to my hometown every vacation"]
    return render_template("hobby.html", hobbies=hobbies)

@app.route("/opinion/<topic>")
@app.route("/opinions/<topic>")
def opinion(topic):
    return "Opinion Page"

@app.route("/opinion/food")
def food():
    foods = ["Chicken", "Pork", "Pasta"]
    return render_template("food.html", foods=foods)

@app.route("/skills/")
def skills():
    skill_levels = {
        "Driving": "Intermediate",
        "Eating": "Professional",
        "Coding": "Beginner"
    }
    return render_template("skill.html", skills=skill_levels)

app.run()
