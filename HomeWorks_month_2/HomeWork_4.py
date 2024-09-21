from random import randint, choice


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        hero = choice(heroes)
        self.__defence = hero.ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                if type(hero) == Berserk and self.defence != hero.ability:
                    blocked = choice([5, 10])
                    hero.blocked_damage = blocked
                    hero.health -= (self.damage - blocked)
                else:
                    hero.health -= self.damage

    def __str__(self):
        return 'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def apply_super_power(self, boss, heroes):
        pass

    def attack(self, boss):
        boss.health -= self.damage


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'CRITICAL_DAMAGE')

    def apply_super_power(self, boss, heroes):
        coefficient = randint(2, 5)
        boss.health -= self.damage * coefficient
        print(f'Warrior {self.name} hit critically {self.damage * coefficient}')


class Magic(Hero):
    def __init__(self, name, health, damage, boost_damage):
        super().__init__(name, health, damage, 'BOOST')
        self.__boost_damage = boost_damage

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.damage += self.__boost_damage
                hero.health += 20  # Лечение на 20 единиц
        print(f'Magic {self.name} boosted all heroes by {self.__boost_damage} damage and healed them by 20 health.')


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BLOCK_AND_REVERT')
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss, heroes):
        boss.health -= self.__blocked_damage
        print(f'Berserk {self.name} reverted {self.__blocked_damage} damage.')


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, 'HEAL')
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.health += self.__heal_points


class Witcher(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'REVIVE')
        self.__has_revived = False

    def apply_super_power(self, boss, heroes):
        if not self.__has_revived:
            for hero in heroes:
                if hero.health <= 0:
                    hero.health = self.health
                    self.health = 0
                    self.__has_revived = True
                    print(f'Witcher {self.name} sacrificed himself to revive {hero.name}!')
                    break

    def attack(self, boss):
        print(f'Witcher {self.name} does not attack.')


class Hacker(Hero):
    def __init__(self, name, health, damage, steal_amount):
        super().__init__(name, health, damage, 'STEAL_AND_TRANSFER')
        self.__steal_amount = steal_amount

    def apply_super_power(self, boss, heroes):
        if boss.health > self.__steal_amount:
            boss.health -= self.__steal_amount
            recipient = choice([hero for hero in heroes if hero.health > 0])
            recipient.health += self.__steal_amount
            print(f'Hacker {self.name} stole {self.__steal_amount} health from Boss and transferred it to {recipient.name}.')
        else:
            print(f'Hacker {self.name} tried to steal health, but Boss does not have enough health.')



class Samurai(Hero):
    def __init__(self, name, health, damage,virus_shuriken_damame,vaccine_shuriken_heal):
        super().__init__( name, health, damage,'SHURIKEN')
        self.__virus_shuriken_damame = virus_shuriken_damame
        self.__vaccine_shuriken_heal = vaccine_shuriken_heal

    def apply_super_power(self, boss, heroes):
        type_of_shuriken = choice(['VIRUS', 'VACCINE'])
        if type_of_shuriken == 'VIRUS':
            boss.health-=self.__virus_shuriken_damame
            print(f'Samurai {self.name} used VIRUS shuriken causing {self.__virus_shuriken_damame} damage to Boss.')
        elif type_of_shuriken=='VACCINE':
            boss.health+=self.__vaccine_shuriken_heal
            print(f'Samurai {self.name} used VACCINE shuriken healing Boss by {self.__vaccine_shuriken_heal} health.')


class King(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'CALL_SAITAMA')

    def apply_super_power(self, boss, heroes):
        if randint(1, 10) == 1:  # 10% шанс
            saitama = Saitama(name='Saitama', health=1000, damage=1000)
            print(f'King {self.name} has summoned Saitama!')
            saitama.attack(boss)
        else:
            print(f'King {self.name} did not summon Saitama this time.')


class Saitama(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'ONE_PUNCH')

    def attack(self, boss):
        boss.health = 0  # Убивает Босса одним ударом
        print(f'Saitama {self.name} defeated the Boss with one punch!')

round_number = 0


def is_game_over(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
        return True
    return False


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if hero.health > 0 and boss.health > 0 and hero.ability != boss.defence:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    show_statistics(boss, heroes)


def show_statistics(boss, heroes):
    print(f'---------- ROUND {round_number} ----------')
    print(boss)
    for hero in heroes:
        print(hero)


def start_game():
    boss = Boss(name='Elena', health=1000, damage=50)

    warrior_1 = Warrior(name='Ahiles', health=280, damage=10)
    warrior_2 = Warrior(name='Helios', health=290, damage=15)
    magic = Magic(name='Potter', health=260, damage=10, boost_damage=30)
    berserk = Berserk(name='Guts', health=240, damage=5)
    doc = Medic(name='Merlin', health=200, damage=5, heal_points=15)
    assistant = Medic(name='Marin', health=300, damage=5, heal_points=5)
    witcher = Witcher(name='Geralt', health=300, damage=0)
    hacker = Hacker(name='Anonymous', health=250, damage=10, steal_amount=50)
    samurai = Samurai(name='Champlu',health=280,damage=20,virus_shuriken_damame=20,vaccine_shuriken_heal=20)
    king = King(name='Artur', health=250,damage=0)

    heroes_list = [warrior_1, doc, warrior_2, magic, berserk, assistant, witcher, hacker,samurai,king]

    show_statistics(boss, heroes_list)
    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


start_game()
