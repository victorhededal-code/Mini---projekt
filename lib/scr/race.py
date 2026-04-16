from race_dicts import aasimar_dict, dragonborn_dict, dwarf_dict, elf_dict, gnome_dict, goliath_dict, halfling_dict, human_dict, orc_dict, tiefling_dict,

class Race:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def print_sheet(self):
        print("=" * 50)
        print(f"RACE: {self.name.upper()}")
        print("=" * 50)

        creature_type = self.data.get("CreatureType") or self.data.get("Creature Type")
        speed = self.data.get("Speed")

        print(f"{'Type':<12}: {creature_type}")

        print("Size(s)     :")
        for key in ["Small", "Medium", "Large"]:
            if key in self.data:
                print(f"  - {key}: {self.data[key]}")

        print(f"{'Speed':<12}: {speed}")

        print("\nFeatures:")

        ignore_keys = ["CreatureType", "Creature Type", "Speed", "Small", "Medium", "Large"]

        i = 1
        for key, value in self.data.items():
            if key not in ignore_keys:
                print(f"\n{i}. {key}")
                print(f"   {value}")
                i += 1

        print("=" * 50)


human = Race("Human", human_dict)
dwarf = Race("Dwarf", dwarf_dict)

human.print_sheet()
dwarf.print_sheet()