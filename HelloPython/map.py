#Ф-ция map() принимает на вход два аргумента: саму фун-цию, которую передаем, и объект.
#Применяет фун-цию, которую передаем, ко всем элементам объекта и возвращает.

list_1 = [x for x in range(1, 20)] #генератор списка
print(list_1)

list_1 = list(map(lambda x: x + 10, list_1))
print(list_1)

#Задача: с клавиатуры вводится некий набор чисел, в качестве разделителя
#используется пробел. Этот набор чисел будет считан в качестве строки. 
#Как превратить лист строк в лист чисел? .split()

data = '15 678 96 15 13'
print(data)

data = list(map(int, data.split()))
print(data)

#Из lambda.py везде, где есть select, изменим на map, получится:

def where(f, col):
    return[x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)  #2, 8, 38

res = list(map(lambda x: (x, x**2), res))  #возвращаем кортеж - х и х в квадрате
print(res)