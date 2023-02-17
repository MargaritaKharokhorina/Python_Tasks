#Задача 32: Определить индексы элементов массива (списка),
#значения которых принадлежат заданному диапазону (т.е. не
#меньше заданного минимума и не больше заданного максимума)
#Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9,
#0, -5, -5, 7]
#Вывод: [1, 9, 13, 14, 19]

# рандомное заполнение списка
from random import randint

n = int(input('n = '))
min_number = int(input('Задайте минимум диапозона: '))
max_number = int(input('Задайте максимум диапозона: '))

list = [randint(1, 10) for i in range(n)]
print(list)

for i in range(len(list)):
    if min_number <= list[i] <= max_number:
        print([i])
