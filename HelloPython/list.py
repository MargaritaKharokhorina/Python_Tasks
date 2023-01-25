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