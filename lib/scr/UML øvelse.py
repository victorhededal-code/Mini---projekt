class Hero:
    def __init__(self, name, level, experience):
        self.name = name
        self.level = level
        self.experience = experience
        self.weapon = []

    def attack(self, weapon):
        atkDamage = 1 + weapon.damage
        print(f"{self.name} gør {atkDamage} skade til X")

    def gainExp(self):
        gainExpValue = 50
        self.experience += gainExpValue
        print(f"{self.name} gains {gainExpValue} experience!")

    def level(self):
        if self.experience > 999:
            self.experience = 0
            self.level += 1
            print(f"{self.name} er nu level {self.level}!")


class inventory:
    def __init__(self, items, weapons, coins):
        self.items = items
        self.weapons = weapons
        self.coins = coins
        self.inventory = []

    def addItem(self, treasure):
        inventory.append(treasure.item, treasure.artifacts, treasure.coins)
        print(f"{treasure.item} added to inventory!")

    def removeItem(self, treasure):
        inventory.remove(treasure.item, treasure.artifacts, treasure.coins)
        print(f"{treasure.item} removed from inventory!")

    def addWeapons(self, weapons, armor, healing_potion, magic_weapon):
        print("buh")

class treasure:
    def __init__(self, items, artifacts, coins):
        self.items = items
        self.artifacts = artifacts
        self.coins = coins

class weapon:
    def __init__(self, damage, durability):
        self.damage = damage
        self.durability = durability

class armor:
    def __init__(self, armor, magic_resistance, durability):
        self.armor = armor
        self.magic_resistance = magic_resistance
        self.durability = durability

class healing_potion:
    def __init__(self, heal, quantity):
        self.heal = heal
        self.quantity = quantity

class magic_weapon:
    def __init__(self, damage, magic_damage, durability):
        self.damage = damage
        self.magic_damage = magic_damage
        self.durability = durability
