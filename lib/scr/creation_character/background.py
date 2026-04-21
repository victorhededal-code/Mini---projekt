from background_dict import *


class Background:
    def __init__(self, name, background):
        self.name = name
        self.background = background
    def __background_move__(self):
        for i in soldier:
            print(i, ':', soldier[i])