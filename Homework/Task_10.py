# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которое нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

coins = int(input("Введите количество монет: "))
reshka = int(input("Сколько монет лежат решкой вверх: "))
emblem = int(input("Сколько монет лежат гербом вверх: "))


def reversal(coins, reshka, emblem): 
    if reshka + emblem == coins:
        if reshka > emblem:
            print('Минимальное количество монет, которое нужно перевернуть:', (coins) - (reshka))
        elif emblem > reshka:
            print('Минимальное количество монет, которое нужно перевернуть:', (coins) - (emblem))
    else:
        print('Решения нет')

reversal(coins, reshka, emblem)
    
      