from lib.scr.background_dict import *
from StatRoller import *

class Background:
    def __init__(self, name, background):
        self.name = name
        self.background = background
    def __background_move__(self):
        for y in soldier:
            for i in soldier[y]:
                # Når det skal på Character_sheets ændre til overfør data (Insert into(?))
                print(i,':',soldier[y][i])