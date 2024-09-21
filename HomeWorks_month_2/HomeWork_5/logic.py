from random import randint
from decouple import config

start = int(config('start'))
end = int(config('end'))
initial_balance = int(config('initial_capital'))

def logic():

    global initial_balance
    number = randint(start, end)
    print('Добро пожаловать на игру "Угадай число"!')
    print("Я загадал число от", start, "до", end)
    print(f'Ваш баланс {initial_balance}')

    while initial_balance > 0:
        print("На какую цифру вы хотите поставить ставку ?")
        letter = int(input())
        if letter < start or letter > end:
            print("Неверный ввод")
            break

        print("Введите сколько вы хотите поставить на эту цифру ?")
        suma = int(input())
        if suma > initial_balance or suma < 1:
            print("Неверный ввод")
            break

        if letter == number:
            print(f"Поздравляю! Вы угадали число: {number} и получили {suma} баллов\n")
            initial_balance += suma
        else:
            print(f"К сожалению, вы не угадали число: {number} и потеряли {suma} баллов\n")
            initial_balance -= suma

        if initial_balance > 0:
            play = input(f'Хотите ли вы поставить еще ставку? Ваш баланс {initial_balance}.\n(yes/q)')
            if play == 'yes':
                continue
            elif play == 'no':
                break
        else:
            print("Ваш баланс истек.")

    print("\nИгра завершена. Поздравляем! Ваш баланс:", initial_balance)

if __name__ == '__main__':
    logic()