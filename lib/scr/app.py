from flask import Flask, request, render_template
from character_creation import create_character

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":

        # Collect form data
        form = request.form

        data = {
            "name": form.get("name"),
            "class": form.get("class"),
            "level": form.get("level"),
            "race": form.get("race"),
            "background": form.get("background"),
            "stats": {
                "STR": int(form.get("str")),
                "DEX": int(form.get("dex")),
                "CON": int(form.get("con")),
                "INT": int(form.get("int")),
                "WIS": int(form.get("wis")),
                "CHA": int(form.get("cha")),
            }
        }

        character = create_character(data)

        return render_template("result.html", character=character)

    return render_template("create_character.html")



app.run(debug=True)