# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

# x = int(input('Первое число: '))
# y = int(input('Второе число: '))
x, y = map(int, input('Введите два числа через пробел: ').split())
z = 0
for i in range(x + y):
    if z:
        break
    for j in range(x + y):
        if i + j == x and i * j == y:
            z = 1
            print('Сумма и произведение: ', *sorted([i, j]))   # Функция sorted() возвращает новый отсортированный список итерируемого объекта (списка, словаря, кортежа).
            break                                              # По умолчанию она сортирует его по возрастанию.
                                                               # Оператор * здесь используется для распаковки итерируемого объекта в аргументы вызова:
                                                               # передаются все элементы списка.
