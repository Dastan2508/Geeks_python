class Transport:
    def __init__(self, the_year, the_model, the_color):
        self.year = the_year
        self.model = the_model
        self.color = the_color

    def change_color(self, new_color):
        print(f'Changed color from {self.color} to {new_color}')
        self.color = new_color


class Plane(Transport):
    def __init__(self, the_year, the_model, the_color):
        super().__init__(the_year, the_model, the_color)  # constructor matching


class Car(Transport):
    counter = 0

    # constructor               # parameters
    def __init__(self, the_year, the_model, the_color, penalties=0):
        # fields / attributes
        super().__init__(the_year, the_model, the_color)
        self.penalties = penalties
        Car.counter += 1

    # method
    def drive(self):
        print(f'Car {self.model} is driving')

    # method
    def signal(self, number_of_times, sound):
        while number_of_times > 0:
            print(f'Car {self.model} is signaling {sound}')
            number_of_times -= 1


class Truck(Car):
    counter = 0
    def __init__(self, the_year, the_model, the_color, penalties=0, load_capacity=0):
        super().__init__(the_year, the_model, the_color, penalties)
        self.load_capacity = load_capacity
        Truck.counter += 1

    def load_cargo(self, type_of_product, weight):
        if self.load_capacity < weight:
            print(f'You can not load more than {self.load_capacity} kg.')
        else:
            print(f'You loaded cargo of {type_of_product} {weight} kg.')


number = 7
print(number)

bmw_car = Car(2020, 'BMW X6', 'red')
print(bmw_car)
print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year} COLOR: {bmw_car.color} PENALTIES: {bmw_car.penalties}')
# bmw_car.color = 'green'
bmw_car.change_color('green')
print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year} NEW COLOR: {bmw_car.color} PENALTIES: {bmw_car.penalties}')

honda_car = Car(2021, 'Honda Fit', 'blue', 500)
print(f'MODEL: {honda_car.model} YEAR: {honda_car.year} COLOR: {honda_car.color} '
      f'PENALTIES: {honda_car.penalties}')

ford_car = Car(the_model='Ford Focus', the_color='silver', penalties=100, the_year=2009)
print(f'MODEL: {ford_car.model} YEAR: {ford_car.year} COLOR: {ford_car.color} '
      f'PENALTIES: {ford_car.penalties}')

bmw_car.drive()
bmw_car.signal(3, 'beep')
ford_car.signal(2, 'Krya')

boeing_plane = Plane(2024, 'Boeing 747', 'white')
print(f'MODEL: {boeing_plane.model} YEAR: {boeing_plane.year} COLOR: {boeing_plane.color}')

man_truck = Truck(2019, 'MAN 300', 'black', 900, 25000)
print(f'MODEL: {man_truck.model} YEAR: {man_truck.year} COLOR: {man_truck.color} '
      f'PENALTIES: {man_truck.penalties} LOAD CAPACITY: {man_truck.load_capacity}')
man_truck.load_cargo('apples', 30000)
man_truck.load_cargo('bananas', 20000)
man_truck.drive()

print('End of program')
print('Bye bye')