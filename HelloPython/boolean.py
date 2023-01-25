f = True
print(f)
# f = False
# print(f)

a = 1 < 4 and 5 > 2 # оба истина
print(a)

a = 1 != 2
print(a)

a = 'qwe'
b = 'qwe'
print (a == b) # сравнение

# сравнение списков
c = [1, 2]
d = [1, 3]
print(c == d)

# тройные (и четверные тоже можно) неравенства
a = 1 < 3 < 5
print(a)

func = 1
T = 4
x = 123
print(func < T < x)

f = 1 > 2 or 4 < 6 # хотя бы одно истина
print(f)

g = [1, 2, 3, 4]
print(g)
print(2 in g) # true, так как 2 есть в списке

# проверка четности числа
# is_odd = g[0] % 2 == 0
# print(is_odd) false, так как g[0] == 1
is_odd = not g[0] % 2
print(is_odd)


