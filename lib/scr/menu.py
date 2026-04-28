from lib.scr.character_creation import *
def menu():
    print("Welcome to the DnD character creator")
    users={}
    person=log_in()
    if person in users:
        character_list=users[person]
    else:
        character_list={}
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