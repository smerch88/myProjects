from random import randint


class Hero:

    def __init__(self, name, rank=1, phrase="", money=50):
        self.name = name
        self.health = 100
        self.rank = rank
        self.power = 10
        self.phrase = phrase
        self.money = money
        self.defence = 10
        self.sword = 0
        self.shield = 0

    def hit(self, other_hero):
        if other_hero.health >= 5:
            if self.power >= self.health / 10:
                self.power = self.health / 10
                other_hero.health -= ((self.power + self.sword) / ((other_hero.defence + other_hero.shield) / 10))
            elif self.power < self.health / 10:
                other_hero.health -= (self.power + self.sword)
        elif other_hero.health <= 5:
            if self.power >= self.health / 10:
                self.power = self.health / 10
                other_hero.health -= ((self.power + self.sword) / ((other_hero.defence + other_hero.shield) / 10))
            elif self.power < self.health / 10:
                other_hero.health -= self.power

        if 0 < self.health < 5:
            self.phrase = 'I surrender!'
        elif self.health == 0:
            self.money -= 50
            other_hero.money += 50
            self.phrase = 'Dead.'

            # @property

    # def name(self):
    #     return self._name

    @property
    def health(self):
        return self._health

    @property
    def rank(self):
        return self.__rank

    @rank.setter
    def rank(self, value):
        if value in [1, 2, 3]:
            self.__rank = value
        else:
            raise Exception

    @health.setter
    def health(self, health):
        if health < 0:
            self._health = 0
        elif health > 100:
            self._health = 100
        else:
            self._health = health


class Mage(Hero):
    # def __init__(self, health=80):
    #     Hero.__init__(self)
    #     self.health = health

    def heal(self, other_hero):
        if other_hero.money >= 10:
            other_hero.health += 10
            other_hero.money -= 10
            self.money += 10
        else:
            print(f'You are dead, not possible to heal, {other_hero.name}.')


class Arena:
    # def __init__(self, fighter1, fighter2):
    #     self.fighter1 = fighter1
    #     self.fighter2 = fighter2

    @staticmethod
    def mortal_combat(fighter1, fighter2):
        if randint(1, 2) == 1:
            fighter1.hit(fighter2)
        elif randint(1, 2) == 2:
            fighter2.hit(fighter1)


class WeaponGen:

    # def __init__(self, shield_name, sword_name):
    #     self.sword_name = sword_name
    #     self.shield_name = shield_name

    @staticmethod
    def give_sword(hero, sword_name, sword_id=[]):
        if hero.sword == 0:
            hero.sword = randint(1, 10)
            sword_id.append(sword_name)
            print(sword_id)
        else:
            print('already have a sword')

    @staticmethod
    def give_shield(hero, shield_name, shield_id=[]):
        if hero.shield == 0:
            hero.shield = randint(1, 10)
            shield_id.append(shield_name)
            print(shield_id)
        else:
            print('already have a shield')


def show_all(hero_list):
    for i in hero_list:
        print(f'Name: {i.name}. Health: {i.health}. Power: {i.power}. Rank: {i.rank}. Money: {i.money}. {i.phrase}')
    return print('\n', end='')


# __________________________________________________________________________________________________________________


Hero1 = Hero('Paladin', 3)
Hero2 = Hero('Mountain King')
Hero3 = Mage('ArchMage')

# Hero1.rank = 3
#
Hero1.hit(Hero2)
Hero1.hit(Hero2)
Hero1.hit(Hero2)
Hero1.hit(Hero2)
Hero1.hit(Hero2)
Hero1.hit(Hero2)
Hero1.hit(Hero2)
Hero1.hit(Hero2)
Hero1.hit(Hero2)


Hero3.hit(Hero1)

Hero2.hit(Hero1)
# __________________________________________________________________________________________________________________

show_all([Hero1, Hero2, Hero3])
Hero3.heal(Hero2)
Hero3.heal(Hero1)

WeaponGen.give_sword(Hero1, 1)
WeaponGen.give_sword(Hero1, 2)


Arena.mortal_combat(Hero1, Hero3)
Arena.mortal_combat(Hero1, Hero3)
Arena.mortal_combat(Hero1, Hero3)
Arena.mortal_combat(Hero1, Hero3)
Arena.mortal_combat(Hero1, Hero3)


# show_all([Hero1, Hero2, Hero3])
# for i in range(12):
#     Arena.mortal_combat(Hero2, Hero1)
#     show_all([Hero1, Hero2, Hero3])

# property  - для уникальности рпедмета попробовать

show_all([Hero1, Hero2, Hero3])