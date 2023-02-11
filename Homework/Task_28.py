#Напишите рекурсивную функцию sum(a,b),
#возвращающую сумму двух целых неотрицательных чисел.
#Из всех арифмитических операций допускаются только +1 и -1.
#Также нельзя использовать циклы.

def sum(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a < 0 or b < 0:
        print('Нужны положительные числа')
    else:
        return sum(a+1, b-1)
    

a, b = map(int, input('Введите два числа через пробел: ').split())
print('Сумма чисел a и b -->', sum(a,b)) 