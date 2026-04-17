from profession_dicts import fighter_dict


class MartialProfession:
    def __init__(self, feature1 = None, feature2 = None, feature3 = None, feature4 = None, feature5 = None, feature6 = None, feature7 = None, feature8 = None, feature9 = None, feature10 = None, feature11 = None, feature12 = None, feature13 = None):
        self.feature1 = feature1
        self.feature2 = feature2
        self.feature3 = feature3
        self.feature4 = feature4
        self.feature5 = feature5
        self.feature6 = feature6
        self.feature7 = feature7
        self.feature8 = feature8
        self.feature9 = feature9
        self.feature10 = feature10
        self.feature11 = feature11
        self.feature12 = feature12
        self.feature13 = feature13
        #eventuelt øg mængden af features i classen, for at akkommodere for flere features i professionen

    def __levelProgression__(self, level):
        pass

class Subclass:
    def __init__(self, name, subfeat1 = None, subfeat2 = None, subfeat3 = None, subfeat4 = None, subfeat5 = None, subfeat6 = None):
        self.name = name
        self.subfeat1 = subfeat1
        self.subfeat2 = subfeat2
        self.subfeat3 = subfeat3
        self.subfeat4 = subfeat4
        self.subfeat5 = subfeat5
        self.subfeat6 = subfeat6

class SpellProfession:
    def __init__(self, spellslots, feature1 = None, feature2 = None, feature3 = None, feature4 = None, feature5 = None, feature6 = None):
        pass

