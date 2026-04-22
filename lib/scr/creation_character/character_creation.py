from lib.scr.creation_character.background import Background
from lib.scr.creation_character.prof.profession_dicts import *
from lib.scr.creation_character.StatRoller import *
from race_dicts import *
from asiapplier import *
def character_create(character_list:list) -> list:
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

        for x in range(1, lvl + 1):
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
        check = input('finished?')
        for i in character:
            print(i, character[i])
        character_list.append(character)
        if check == 'yes' or check == 'y' or check == 'Yes' or check == 'YES' or check == 'Y' or check == '':
            return character_list
character_list = []
character_list =character_create(character_list)