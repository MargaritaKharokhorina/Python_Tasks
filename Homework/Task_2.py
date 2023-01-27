# Задача 2: Найдите сумму цифр трехзначного числа. 
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input('Введите трехзначное число: '))

if 99 < number < 1000:
    digit3 = number % 10
    number = number // 10
    digit2 = number % 10
    number = number // 10
    print(f'{number} + {digit2} + {digit3}')
    print("Сумма цифр числа:", number + digit2 + digit3)
else:
    print("Вы ввели не трехзначное число")
