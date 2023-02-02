
colors = {'red', 'green', 'blue'}
print(type(colors)) # тип данных set

# В множества можно добавлять элементы:
colors.add('gray')
print(colors)

# Удалить какой-то элемент:
colors.remove('red')
print(colors)

# Тоже удаление:
colors.discard('blue')
print(colors)

# Очистить множества:
colors.clear()
print(colors)


# Иные операции
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()          # создание множества на основе имеющегося: {1, 2, 3, 5, 8}
print(c)

u = a.union(b)        # объединение множеств {1, 2, 3, 5, 8, 13, 21}
print(u)

i = a.intersection(b) # пересечение {8, 2, 5}
print(i)

dl = a.difference(b)  # разница: 1 - {1, 3} ; 2 - {13, 21}
dr = b.difference(a)
print (dl, dr)

# Неизменяемые множества - frozenset
s = frozenset(a)
print(s)


