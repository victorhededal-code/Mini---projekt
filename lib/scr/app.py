from flask import Flask, request, render_template
from character_creation import create_character
from ServerConnect import *
from profession_dicts import proffesion
from race_dicts import racedict
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
            },
            "id": (form.get("id")),
        }

        character = create_character(data)

        file_path = "characters.json"

        # write JSON
        with open(file_path, "w") as f:
            json.dump([character], f, indent=4)


        load_characters(file_path)

        return render_template("result.html", character=character)

    return render_template("create_character.html")

@app.route("/about_us", methods=["GET"])
def about_us():
    return render_template("about_us.html")

@app.route("/characters", methods=["GET"])
def characters():

    character_id = request.args.get("id")

    if character_id:

        # Export DB character into JSON file
        export_character("upload_pc.json", character_id)

        try:
            with open("upload_pc.json", "r", encoding="utf-8") as f:
                raw = json.load(f)

            # -----------------------------
            # RACE FEATURES
            # -----------------------------
            race_key = raw.get("pc_race")
            race_data = racedict.get(race_key, {})

            race_features = []
            for key, value in race_data.items():
                race_features.append(f"{key}: {value}")

            # -----------------------------
            # CLASS FEATURES
            # -----------------------------
            class_key = raw.get("class_name")
            class_level = raw.get("class_level")

            class_data = proffesion.get(class_key, {})

            class_features = []

            for level, features in class_data.items():
                if level <= class_level:
                    for feature_name, description in features.items():
                        class_features.append(f"Level {level} - {feature_name}: {description}")

            # -----------------------------
            # FINAL CHARACTER FORMAT
            # -----------------------------
            character = {
                "Name": raw.get("pc_name"),
                "Class": class_key,
                "Level": raw.get("class_level"),
                "Race": race_key,
                "Background": raw.get("pc_background"),

                "Stats": {
                    "STR": raw.get("str"),
                    "DEX": raw.get("dex"),
                    "CON": raw.get("con"),
                    "INT": raw.get("intelligence"),
                    "WIS": raw.get("wis"),
                    "CHA": raw.get("cha"),
                },

                "Class Features": class_features,
                "Race Description": race_features,
                "id": raw.get("pc_code")
            }

        except Exception as e:
            print("Error loading character:", e)
            character = None

        return render_template("result.html", character=character)

    # -----------------------------
    # LIST PAGE (no ID)
    # -----------------------------
    file_path = "characters.json"

    if os.path.exists(file_path):
        try:
            characters = load_characters()
        except:
            characters = []
    else:
        characters = []

    return render_template(
        "characters.html",
        characters=characters,
        proffesion=proffesion,
        racedict=racedict
    )

if __name__ == "__main__":
    app.run(debug=True)