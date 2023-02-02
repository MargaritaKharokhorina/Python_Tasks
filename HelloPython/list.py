# В Python нет как таковых массивов, их заменяют списки

# list = [1, 2, 3]
# col = ['1', '2', 'hello']
# print(list)
# print(col)

# Динамическая типизация языка позволяет использовать различные типы в списке:
# list = ['1', '2', 'hello', 1, 2, 3.5, True] - но лучше так не делать :) 

numbers = [1, 2, 3, 4, 5]
print(numbers)
ran = range(1, 6)
print(type(ran))
numbers = list(ran)            # приведение типа range к list
print(type(numbers))

print(numbers)                 # [1, 2, 3, 4, 5]
numbers[0] = 10
print(f'{len(numbers)} len')   # 5 элементов
print(numbers)                 # [10, 2, 3, 4, 5]
for i in numbers:
    i *= 2
    print(i)                   # [20, 4, 6, 8, 10]
print(numbers)                 # [10, 2, 3, 4, 5]

list1 = [1, 2, 3, 4, 5]
list2 = list1

for e in list1:
    print(e)                  # 1, 2, 3, 4, 5

print()

for e in list2:              # 1, 2, 3, 4, 5
    print(e) 

# Теперь поменяем значение первого элемента из списка и снова выведем два списка:
list1[0] = 123
for e in list1:
    print(e)                  # 123, 2, 3, 4, 5

print()

for e in list2:               # 123, 2, 3, 4, 5 --> элемент[0] поменялся и во втором списке
    print(e)

# Аналогично будет, если поменяем значение во втором списке (в первом тоже изменится):
list2[1] = 333
for e in list1:
    print(e)                  # 123, 333, 3, 4, 5

print()

for e in list2:               # 123, 333, 3, 4, 5 --> элемент[0] поменялся и во втором списке
    print(e)


print()
# Как удалять последний элемент списка (метод pop извлекает последний элемент):
print(len(list1))  # смотрим, сколько элементов
print(list1.pop()) # удаляем
print(list1)       # результат [123, 333, 3, 4]

print()
# Если нужно удалить конкретный элемент, делаем это путем передачи индекса:
print(list1.pop(2)) 
print(list1)      # [123, 333, 4]

# Вставить нужный элемент на определенную позицию - insert :
print(list1.insert(2, 11))
print(list1)      # [123, 333, 11, 4] 

# Добавление элемента в конец - функцией append:
print(list1.append(9))  
print(list1)       # [123, 333, 11, 4, 9]       
