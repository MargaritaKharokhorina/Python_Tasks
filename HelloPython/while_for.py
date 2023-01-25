# Цикл while позволяет выполнить блок операторов какое-то количество раз

original = 23
print(original)
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)

# Управляющая конструкция while-else

original = 23
print(original)
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Пожалуй,')
    print('хватит')
print(inverted)

# Цикл for

for i in 1,2,3,4,5: # работает и со строками
    print(i**2)

r = range(10)
for i in r:
    print(i)
