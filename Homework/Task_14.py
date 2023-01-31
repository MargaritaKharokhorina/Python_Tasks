# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2 в степени k), не превосходящие числа N.
# 10 -> 1 2 4 8

number = int(input("Введите положительное число: ")) 
extent = 1
result = 1

while result <= number:
    print(result)
    result = 2 ** extent
    extent+=1   
