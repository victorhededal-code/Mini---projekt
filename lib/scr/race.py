from race_dicts import human_dict, dwarf_dict

class Race:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def print_sheet(self):
        print("=" * 50)
        print(f"RACE: {self.name.upper()}")
        print("=" * 50)

        # --- Basic info ---
        creature_type = self.data.get("CreatureType") or self.data.get("Creature Type")
        speed = self.data.get("Speed")

        print(f"{'Type':<12}: {creature_type}")

        # Print all size types (Small, Medium, etc.)
        print("Size(s)     :")
        for key in ["Small", "Medium", "Large"]:
            if key in self.data:
                print(f"  - {key}: {self.data[key]}")

        print(f"{'Speed':<12}: {speed}")

        # --- Features ---
        print("\nFeatures:")

        # keys that are NOT features
        ignore_keys = ["CreatureType", "Creature Type", "Speed", "Small", "Medium", "Large"]

        i = 1
        for key, value in self.data.items():
            if key not in ignore_keys:
                print(f"\n{i}. {key}")
                print(f"   {value}")
                i += 1

        print("=" * 50)


# Create races
human = Race("Human", human_dict)
dwarf = Race("Dwarf", dwarf_dict)

# Print sheets
human.print_sheet()
dwarf.print_sheet()