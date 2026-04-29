from menu import menu
import json

def reset_json(file_path="characters.json"):
    with open(file_path, "w") as f:
        json.dump([], f)

if __name__ == "__main__":
    reset_json()
    while True:
        menu()