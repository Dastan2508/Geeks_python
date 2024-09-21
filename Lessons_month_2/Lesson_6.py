animals_list = ['cat', 'dog', 'cow', 'rabbit']
fruits_list = ['banana', 'apple']

# O (A + F)
for animal in animals_list:
    print(animal)

for fruit in fruits_list:
    print(fruit)

print('-------------------')
# O (A * F)
for animal in animals_list:
    for fruit in fruits_list:
        print(f'{animal} likes {fruit}')

a = len(animals_list)
while a > 0:
    a = a - 1
    print(a)
    for animal in animals_list:
        print(animal)
# O (A * A) => O (A**2)

for fruit in fruits_list:
    print(fruit)
    b = 0
    while b < len(fruits_list):
        print(fruits_list[b])
        b = b + 1
    for animal in animals_list:
        print(animal)
# O (F * (F + A)) => O (F**2 + F * A)

for i in [3, 2, 1, 0]:
    print(i)

print('-----------')
def counter(num):
    print(num)
    if num > 0:
        counter(num - 1)

counter(3)