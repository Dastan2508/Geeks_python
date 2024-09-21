class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__was_born()

    def __was_born(self):
        print(f'Animal {self.__name} was born')

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if type(age) == int and age > 0:
            self.__age = age
        else:
            raise ValueError('Age must be a positive integer')

    def info(self):
        return f'{self.__name} is {self.__age} years old. Birth year is {2024 - self.__age}'

    def voice(self):
        pass


class Dog(Animal):
    def __init__(self, name, age, commands):
        # super().__init__(name, age)
        super(Dog, self).__init__(name, age)
        self.__commands = commands

    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, commands):
        self.__commands += commands

    def info(self):
        return super().info() + f'\nCommands: {self.__commands}'

    def voice(self):
        print('Gav')


class Cat(Animal):
    def __init__(self, name, age):
        super(Cat, self).__init__(name, age)

    def voice(self):
        print('Myau')


class FightingDog(Dog):
    def __init__(self, name, age, commands, wins):
        super(FightingDog, self).__init__(name, age, commands)
        self.__wins = wins

    @property
    def wins(self):
        return self.__wins

    @wins.setter
    def wins(self, value):
        self.__wins = value

    def fight(self):
        print(f'Dog {self.get_name()} is fighting. This dog has {self.__wins} wins.')

    def info(self):
        return super().info() + f'\nWins: {self.__wins}'

    def voice(self):
        print('Rrr gav')


class Fish(Animal):
    def __init__(self, name, age):
        super(Fish, self).__init__(name, age)


# some_animal = Animal('Anim', 3)
# some_animal.set_age(4)
# print(some_animal.get_name())
# print(some_animal.info())

cat = Cat('Tom', 1)
# print(cat.info())

dog = Dog('Snooppy', 5, ['sit', 'run'])
dog.commands = ['bark']
# print(dog.commands)
# print(dog.info())

fighting_dog = FightingDog('Tayson', 2, ['fight'], 10)
fighting_dog.fight()
# print(fighting_dog.info())

# fish = Fish('Nemo', 7)
#    a = b

animals_list = [cat, dog, fighting_dog, Fish('Nemo', 7)]
for animal in animals_list:
    print(animal.info())
    animal.voice()