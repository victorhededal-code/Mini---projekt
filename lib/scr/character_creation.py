# character_creation.py

from background import Background
from profession_dicts import proffesion
from StatRoller import stats
from race_dicts import racedict
from asiapplier import apply_asi
from background import backgrounds


def create_character(data: dict) -> dict:
    """
    Create a character from provided data (from Flask request).
    """

    character = {}

    # --- Basic Info ---
    name = data.get("name", "Unknown")
    char_class = data.get("class", "").lower()
    level = int(data.get("level", 1))
    race = data.get("race", "").lower()
    background_name = data.get("background", "")

    # --- Stats ---
    # Use provided stats or roll new ones
    if "stats" in data:
        character_stats = data["stats"]
    else:
        character_stats = stats()

    # --- Assign Base Info ---
    character["Name"] = name
    character["Class"] = char_class
    character["Level"] = level
    character["Race"] = race

    # --- Class Features ---
    class_features = []
    if char_class in proffesion:
        for lvl in range(1, level + 1):
            features = proffesion[char_class].get(lvl, {})
            for key, value in features.items():
                class_features.append(f"{key}: {value}")

    character["Class Features"] = class_features

    # --- Race Info ---
    if race in racedict:
        character["Race Description"] = racedict[race]
    else:
        character["Race Description"] = "Unknown race"

    # --- Background ---
    if background_name in backgrounds:
        bg = Background(name, background_name)
        Background.__background_move__(bg)

        character["Background"] = background_name

        # Apply ASI if available
        try:
            asi = backgrounds[background_name]["ASI"]
            character_stats = apply_asi(character_stats, asi)
        except Exception:
            pass
    else:
        character["Background"] = background_name or "None"

    # --- Final Stats ---
    character["Stats"] = character_stats

    return character