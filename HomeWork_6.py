"""bubble_sort"""
def bubble_sort(mass):
    n = len(mass) - 1
    s = 0
    while n > 0:
        for i in range(n):
            if mass[i] > mass[i + 1]:
                mass[i], mass[i + 1] = mass[i + 1], mass[i]
                s += 1
        n -= 1
        print(mass)
    print('=' * 80)
    return mass, s

a = [6, 12, 5, 3, 10, 3, 1, 6, 8, 9, 7, 2, 41]
sort_a, s_turn = bubble_sort(a)
print(sort_a)
print(s_turn)




"""binary_search"""
def binary_search(arr, val):
    N = len(arr)
    ResultOk = False
    First = 0
    Last = N - 1
    Pos = -1

    while First <= Last:
        Middle = (First + Last) // 2
        if arr[Middle] == val:
            ResultOk = True
            Pos = Middle
            break
        elif arr[Middle] < val:
            First = Middle + 1
        else:
            Last = Middle - 1

    if ResultOk:
        print(f"Элемент найден на позиции {Pos}")
        return Pos
    else:
        print("Элемент не найден")
        return -1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
value = 7
binary_search(array, value)


