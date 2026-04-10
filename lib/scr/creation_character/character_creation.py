from level import lvl_calc
from proffesion import proff_calc
from race import race_calc
def character_create(character_list:list) -> list:
    "goes through a character creation process"
    while True:
        character = {}
        name = input('Choose your character name')
        character['name', name]
        proff = input ('choose class: \nclass1 \nclass2 \nclass3 \nosv…')
        character['class', proff_calc(proff)]
        race=input('choose Race / Species:\nSpecies1 \nSpecies2 \nSpecies3 \nSpecies4')
        character['race', race_calc(race)]
        lvl=int(input('choose level'))
        character['lvl:',lvl]
        character['stats:',lvl_calc(lvl)]
        back= input('input your characters background here')
        character['background', back]
        align = input('Choose your characters alignment here')
        character['alignment', align]
        check = input('finished?')
        if check == 'yes' or check == 'y' or check == 'Yes' or check == 'YES' or check == 'Y':
            character_list[character]
            return character_list




