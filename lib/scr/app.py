from flask import Flask, request, render_template
from character_creation import create_character
import json
import os

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
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
        file_path = "characters.json"
        characters = [character]

        with open(file_path, "w") as f:
            json.dump(characters, f, indent=4)

        return render_template("result.html", character=character)

    return render_template("create_character.html")

@app.route("/characters")
def characters():
    file_path = "characters.json"
    characters = []
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            try:
                characters = json.load(f)
            except:
                characters = []
    return render_template("characters.html", characters=characters)

if __name__ == "__main__":
    app.run(debug=True)