# Управляющие конструкции на примере нахождения максимума из двух чисел

a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)

# if в связке с блоком elif 

username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это же МАША!')
elif username == 'Рита':
    print('Рита, так держать!')
elif username == 'Иван':
    print('Иван крутой :)')
else:
    print('Привет,', username)