def apply_asi(statblock, asi_data):
    choices = asi_data["choose"]
    bonuses = asi_data["bonuses"]

    print(f"You can improve: {choices}")
    print(f"Bonuses to assign: {bonuses}")

    for bonus in bonuses:
        while True:
            choice = input(f"Where do you want to add +{bonus}? ").upper()
            if choice in choices:
                statblock[choice] += bonus
                print(f"{choice} increased to {statblock[choice]}")
                break
            else:
                print("Invalid choice, try again.")

    return statblock