from background import Background
from profession_dicts import *
from StatRoller import *
from race_dicts import *
from asiapplier import *
from features import *
def character_create(character_list:dict) -> dict:
    "goes through a character creation process"
    while True:
        character = {}
        name = input('Choose your character name')
        character['Name:'] = name
        character_stats = stats()
        print('choose class:\n Fighter \n Champion')
        proff = input ()
        character['Class:'] = proff
        proff = proff.lower()
        lvl=int(input('choose level'))
        character['LVL:']=lvl
        if lvl >= 4:
            lvl4opt=input("Would you like to \n 1. Pick a feat \n 2. Upgradabe ilityscore \n Pick a number: ")

            if lvl4opt == "1":
                for key in featuredict:
                    print(key)
                featopt=input("Choose feature")
            elif lvl4opt == "2":

            else:
                print("error")
                pass

        for x in range(1, +-lvl + 1):
            for i in proffesion[proff][x]:
                print(i, ':', proffesion[proff][x][i])
        race=input('choose Race / Species: \nHuman\n elf\n gnome\n a fucking dragon')
        if race in racedict:
            print(f"{racedict[race]}")
        character['Race:']= race
        back= input('input your characters background here')
        if back in backgrounds:
            char = Background(name,back)
            Background.__background_move__(char)
            character['Background:'] = back
            character_stats = apply_asi(character_stats, back["ASI"])
            print(character_stats)
        align = input('Choose your characters alignment here')
        character['Alignment:'] = align
        character['Stats:\n'] = character_stats
        for i in character:
            print(i, character[i])
        character_list[name]=character
        check = input('finished?')
        check=check.lower()
        if check == 'yes' or check == 'y' or check == '':
            return character_list
character_list = []
character_list =character_create(character_list)