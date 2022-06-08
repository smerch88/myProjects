# Дописати нашу реалізацію героїв, що ми почали в класі.
#
# Герой має мати наступні атрибути: ім‘я, здоров‘я, ранг, сила і метод вдарити.
#
# Метод вдарити має наносити шкоду противнику в розмірі сили героя.
#
# Програма має мати наступні обмеження: здоров‘я від 0 до 100, ранг 1,2,3. Сила не більше 10% теперішнього здоров‘я героя. Не можна бити героїв здоров‘я яких менше 5.


class Hero:

    def __init__(self, name, rank=1, power=10, phrase="", money=50):
        self.name = name
        self._health = 100
        self.rank = rank
        self.power = power
        self.phrase = phrase
        self.money = money

    def hit(self, other_hero):
        if other_hero.health >= 5:
            if self.power >= self.health / 10:
                self.power = self.health / 10
                other_hero.health -= self.power
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
        return self._rank

    @rank.setter
    def rank(self, value):
        if value in [1, 2, 3]:
            self._rank = value
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
    def heal(self, other_hero):
        if other_hero.money >= 10:
            other_hero.health += 10
            other_hero.money -= 10
            self.money += 10
        else:
            print('You are dead')


def show_all(hero_list):
    for i in hero_list:
        print(f'Name: {i.name}. Health: {i.health}. Power: {i.power}. Rank: {i.rank}. Money: {i.money}. {i.phrase}')
    return print('\n')
# ______________________________________________________________________________________________________________________


Hero1 = Hero('Paladin')
Hero2 = Hero('Mountain King')
Hero3 = Mage('ArchMage')

Hero1.hit(Hero2)
Hero1.hit(Hero2)
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
# ______________________________________________________________________________________________________________________

show_all([Hero1, Hero2, Hero3])
Hero3.heal(Hero2)
Hero3.heal(Hero1)

show_all([Hero1, Hero2, Hero3])

