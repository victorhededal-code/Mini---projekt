import random
import time


def stats():
    rolls = []
    tries = 0
    statopt = {}
    statblock = {"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}
    while True:
        while tries < 6:
            do=input("Roll with Enter ")
            rolls = [random.randint(1, 6) for _ in range(4)]
            print(f"Rolls: {rolls}")
            rolls.remove(min(rolls))
            stat = sum(rolls)
            print(f"{stat}\n")
            tries+=1
            statopt.update({tries: stat})
    # CHOOSE STRENGTH
        time.sleep(2)
        print(statopt)
        opt=int(input("Which stat do you want in STR?"))
        if opt in statopt.keys():
            trans=statopt.get(opt)
            statblock.update({"STR": trans})
            del statopt[opt]
            print(statblock)
        else:
            print("Invalid input")
    # CHOOSE DEXTERITY
        print(statopt)
        opt=int(input("Which stat do you want in DEX?"))
        if opt in statopt.keys():
            trans=statopt.get(opt)
            statblock.update({"DEX": trans})
            del statopt[opt]
            print(statblock)
        else:
            print("Invalid input")
    # CHOOSE CONSTITUTION
        print(statopt)
        opt=int(input("Which stat do you want in CON?"))
        if opt in statopt.keys():
            trans=statopt.get(opt)
            statblock.update({"CON": trans})
            del statopt[opt]
            print(statblock)
        else:
            print("Invalid input")
    # CHOOSE INTELLIGENCE
        print(statopt)
        opt=int(input("Which stat do you want in INT?"))
        if opt in statopt.keys():
            trans=statopt.get(opt)
            statblock.update({"INT": trans})
            del statopt[opt]
            print(statblock)
        else:
            print("Invalid input")
    # CHOOSE WISDOM
        print(statopt)
        opt=int(input("Which stat do you want in WIS?"))
        if opt in statopt.keys():
            trans=statopt.get(opt)
            statblock.update({"WIS": trans})
            del statopt[opt]
            print(statblock)
        else:
            print("Invalid input")
    # CHOOSE CHARISMA
        print(statopt)
        opt=int(input("Which stat do you want in CHA?"))
        if opt in statopt.keys():
            trans=statopt.get(opt)
            statblock.update({"CHA": trans})
            del statopt[opt]
            print(statblock)
        else:
            print("Invalid input")
        return statblock
