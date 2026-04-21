from lib.scr.creation_character.background import Background
from profession import *
from profession_dicts import *
from lib.scr.creation_character.StatRoller import *
from race_dicts import *
def character_create(character_list:list) -> list:
    "goes through a character creation process"
    while True:
        character = {}
        name = input('Choose your character name')
        character['name'] = name
        print('choose class:\n Fighter \n Champion')
        proff = input ()
        lvl=int(input('choose level'))
        character['lvl:']=lvl
        #character['stats:']= stats()
        if proff == 'Fighter':
            if lvl == 20:
                for i in fighter_dict:
                    for y in fighter_dict[i]:
                        print(y,':',fighter_dict[i][y])
            else:
                if lvl >= 1:
                    for i in fighter_dict[1]:
                        print(i, ':', fighter_dict[1][i])
                if lvl >= 2:
                    for i in fighter_dict[2]:
                        print(i, ':', fighter_dict[2][i])
                if lvl >= 5:
                    for i in fighter_dict[5]:
                        print(i, ':', fighter_dict[5][i])
                if lvl >= 11:
                    for i in fighter_dict[11]:
                        print(i, ':', fighter_dict[11][i])
                if lvl >= 13:
                    for i in fighter_dict[13]:
                        print(i, ':', fighter_dict[13][i])
                if lvl >= 19:
                    for i in fighter_dict[19]:
                        print(i, ':', fighter_dict[19][i])
        elif proff == 'Champion':
            if lvl == 20:
                for i in paladin_dict:
                    for y in paladin_dict[i]:
                        print(y,':',paladin_dict[i][y])
            else:
                if lvl >= 1:
                    for i in paladin_dict[1]:
                        print(i, ':', paladin_dict[1][i])
                if lvl >= 2:
                    for i in paladin_dict[2]:
                        print(i, ':', paladin_dict[2][i])
                if lvl >= 5:
                    for i in paladin_dict[5]:
                        print(i, ':', paladin_dict[5][i])
                if lvl >= 11:
                    for i in paladin_dict[11]:
                        print(i, ':', paladin_dict[11][i])
                if lvl >= 13:
                    for i in paladin_dict[13]:
                        print(i, ':', paladin_dict[13][i])
                if lvl >= 19:
                    for i in paladin_dict[19]:
                        print(i, ':', paladin_dict[19][i])
        else:
            print('Invalid input')
        character['class']= proff
        race=input('choose Race / Species: \nHuman\n elf\n gnome\n a fucking dragon')
        if race== 'Human':
            for i in human_dict:
                print(i,':',human_dict[i])
        character['race']= race
        back= input('input your characters background here')
        char = Background(name,back)
        Background.__background_move__(char)
        character['background'] = back
        align = input('Choose your characters alignment here')
        character['alignment'] = align
        check = input('finished?')
        if check == 'yes' or check == 'y' or check == 'Yes' or check == 'YES' or check == 'Y':
            pass
            return character_list

character_list = []
character_list =character_create(character_list)