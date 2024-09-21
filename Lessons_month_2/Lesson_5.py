# import random
from email.policy import default
from random import randint, choice as get_random_element

import emoji

from utils import calculator as calc
from utils.templates import Person
from termcolor import cprint
from decouple import config

# print(random.randint(1, 6))
print(randint(1, 6))
print(get_random_element([8, 4, 234, 4]))
print(calc.multiplication(6, 3))

my_friend = Person('Jane', 24)
print(my_friend)
cprint("Hello, World!", "green", "on_red")
print(emoji.emojize("Python is fun :red_heart:"))
print(config('DATABASE_URL'))

commented = config('COMMENTED', default=0, cast=int)
print(commented * 2)