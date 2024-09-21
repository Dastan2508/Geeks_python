class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    def __str__(self):
        return f'{self.__name} is {self.age} years old.'


class Car:
    def __init__(self, model, year):
        self.__model = model
        self.__year = year
        self.__owner = None

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if type(value) is Person:
            self.__owner = value

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    def drive(self):
        print(f'Car {self.__model} is driving')

    def __str__(self):
        return (f'MODEL: {self.__model}, YEAR: {self.__year}'
                f'\nOwner: {self.__owner}')

    def __lt__(self, other):
        return self.__year < other.__year

    def __gt__(self, other):
        return self.__year > other.__year

    def __eq__(self, other):
        return self.__year == other.__year

    def __ne__(self, other):
        return self.__year != other.__year

    def __le__(self, other):
        return self.__year <= other.__year

    def __ge__(self, other):
        return self.__year >= other.__year


class FuelCar(Car):
    __total_fuel = 0

    @staticmethod
    def get_fuel_type():
        return 'AI 95'

    @classmethod
    def print_fuel_remain(cls):
        print(f'Factory FUEL CAR has: {cls.__total_fuel} litters of fuel.')

    @classmethod
    def buy_fuel(cls, amount):
        cls.__total_fuel += amount
        cls.print_fuel_remain()

    def __init__(self, model, year, fuel_bank):
        # super().__init__(model, year)
        # super(FuelCar, self).__init__(model, year)
        Car.__init__(self, model, year)
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel -= self.__fuel_bank

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    def drive(self):
        print(f'Car {self.model} is driving by fuel')

    def __str__(self):
        return super().__str__() + f'\nFUEL BANK: {self.__fuel_bank}'

    def __add__(self, other):
        return self.__fuel_bank + other.__fuel_bank


class ElectricCar(Car):
    def __init__(self, model, year, battery):
        Car.__init__(self, model, year)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def drive(self):
        print(f'Car {self.model} is driving by battery')

    def __str__(self):
        return super().__str__() + f'\nBATTERY: {self.__battery}'


class HybridCar(FuelCar, ElectricCar):
    def __init__(self, model, year, fuel_bank, battery):
        FuelCar.__init__(self, model, year, fuel_bank)
        ElectricCar.__init__(self, model, year, battery)


FuelCar.buy_fuel(500)

my_friend = Person('Jane', 25)

audi_car = FuelCar('Audi A6', 2020, 80)
audi_car.owner = my_friend
print(audi_car)

tesla_car = ElectricCar('Tesla Model Y', 2023, 15000)
tesla_car.owner = my_friend
print(tesla_car)

# me =  Person('Jim', 33)
#  a = b

toyota_car = HybridCar('Toyota Highlander', 2019, 70, 10000)
toyota_car.owner = Person('Jim', 33)
print(toyota_car)
toyota_car.drive()

print(HybridCar.mro())

number_1, number_2 = 2, 8
print(f'Number one is greater than number two: {number_1 > number_2}')
print(f'Number one is less than number two: {number_1 < number_2}')
print(f'Audi is less than toyota: {audi_car < toyota_car}')
print(f'Audi is the same with tesla: {audi_car == tesla_car}')

print(f'Sum of numbers: {number_1 + number_2}')
print(f'Sum: {audi_car + toyota_car}')

# FuelCar.total_fuel -= 100
FuelCar.print_fuel_remain()

print(f'Factory FUEL CAR uses {FuelCar.get_fuel_type()} type of fuel.')

print(f'Owner of toyota was born in {2024 - toyota_car.owner.age} year.')