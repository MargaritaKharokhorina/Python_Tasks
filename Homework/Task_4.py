# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

origami_amount = int(input("Введите натуральное число: "))

if origami_amount >= 6:
    origami_boys = origami_amount // 3
    origami_Katya = origami_boys * 2
    origami_Petya = origami_boys // 2
    origami_Serg = origami_boys // 2
    print(f'Петя сделал {origami_Petya} журавликов(ка), Сережа тоже - {origami_Serg}, Катя - {origami_Katya}')
else:
    print('Решения нет, количество журавликов должно быть от шести')

