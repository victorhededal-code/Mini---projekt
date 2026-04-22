from race_dicts import *

class Race:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def print_sheet(self):
        print("=" * 50)
        print(f"RACE: {self.name.upper()}")
        print("=" * 50)

        creature_type = self.data.get("CreatureType", "Unknown")
        speed = self.data.get("Speed")

        print(f"{'Type':<12}: {creature_type}")

        print("Size(s)     :")
        for key in ["Small", "Medium", "Large"]:
            if key in self.data:
                print(f"  - {key}: {self.data[key]}")

        print(f"{'Speed':<12}: {speed}")

        print("\nFeatures:")

        ignore_keys = ["CreatureType", "Creature Type", "Speed", "Small", "Medium",]

        i = 1
        for key, value in self.data.items():
            if key not in ignore_keys:
                print(f"\n{i}. {key}")
                print(f"   {value}")
                i += 1

        print("=" * 50)


races = [
    Race("Human", human_dict),
]

for race in races:
    race.print_sheet()