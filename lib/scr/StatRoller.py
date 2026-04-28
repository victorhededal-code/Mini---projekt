import random
import time
from background_dict import *

def stats():
    statopt = {}
    statblock = {"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}

    # Roll stats
    for i in range(1, 7):
        rolls = [random.randint(1, 6) for _ in range(4)]
        time.sleep(1)
        print(f"Rolls: {rolls}")
        rolls.remove(min(rolls))
        stat = sum(rolls)
        print(f"{stat}\n")
        statopt[i] = stat

    time.sleep(1)

    for ability in statblock.keys():
        while True:
            print(f"Available rolls: {statopt}")
            try:
                opt = int(input(f"Which stat do you want in {ability}? "))
                if opt in statopt:
                    statblock[ability] = statopt.pop(opt)
                    print(statblock)
                    break
                else:
                    print("Invalid choice, try again.")
            except ValueError:
                print("Please enter a number.")

    return statblock




