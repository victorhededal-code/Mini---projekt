class Hero:
    def __init__(self, name, hp, level, experience, weapon):
        self.__name = name
        self.__hp = hp
        self.__level = level
        self.__experience = experience
        self.__weapon = weapon

    def attack(self, monster):
        damage = self.__weapon.damage
        monster.__hp -= damage
        print(f"{self.__name} attacks {monster.__name} with {self.__weapon.name} for {damage} damage!")
        if monster.__hp <= 0:
            print(f"{monster.name} has been defeated!")
            self.gain_experience(monster.experience)

    def gain_experience(self, exp):
        self.experience += exp
        print(f"{self.name} gains {exp} experience points!")
        if self.experience >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience = 0
        self.hp += 20
        print(f"{self.name} has leveled up to level {self.level}! HP increased to {self.hp}.")


class Weapons:
    def __init__(self, Weapon_type, damage_type, usage, damage_value):
        self.Weapon_type = Weapon_type
        self.damage_type = damage_type
        self.usage = usage
        self.damage_value = damage_value

    def show_state(self):
        print(
            f"Weapon Type: {self.Weapon_type}, Damage Type: {self.damage_type}, Usage: {self.usage}, Damage Value: {self.damage_value}")

    def show_damage(self):
        print(f"{self.Weapon_type} deals {self.damage_value} {self.damage_type} damage.")

    def repair(self):
        print(f"{self.Weapon_type} has been repaired and is ready for use again.")


class Reward:
    def __init__(self, exp: int, gold: int):
        self.exp = exp
        self.gold = gold

    def give_exp(self):
        return self.exp

    def give_gold(self):
        return self.gold


class Monster:
    def __init__(self, name: str, hp: int, weakness, reward: Reward, weapon=None):
        self.name = name
        self.hp = hp
        self.weakness = weakness
        self.reward = reward
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            return f"{self.name} attacks with {self.weapon}!"
        return f"{self.name} attacks with claws!"

    def take_damage(self, damage: int):
        self.hp -= damage
        if self.hp <= 0:
            return True
        return False

    def get_reward(self):
        return self.reward
