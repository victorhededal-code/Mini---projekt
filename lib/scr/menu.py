from creation_character.character_creation import *
def menu():
    print("Welcome to the DnD character creator")
    character_list=log_in()
    while True:
        print("Welcome to the DnD character creator")
        ch1 = input("Choose between printing an existing character-sheet or making a new Character-sheet")
        if ch1 == "print":
            character_print()
        elif ch1 == "make":
            character_list=character_create(character_list)


def log_in() -> list:
    pass
def character_print():
    pass