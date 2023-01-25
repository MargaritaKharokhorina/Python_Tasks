# типы данных и переменная 
# int, float, boolean, str, list, None

# value = None
a = 311
b = 3.11
# print(a)
# print(b)
# value = 1234
# print(value)
# Чтобы отобразить тип переменных, используем type:
# print(type(a))
# print(type(b))
# print(type(value))
s = "hello 'python'"
# print(s)

# Способы вывода значений нескольких переменных
# print(a, b, s) - если м/д ними нужно поставить какие-то доп.данные, например, строки, то:
# print(a, '-', b, '-', s);
# Можно использовать форматированный вывод, описав шаблон:
print('{} - {} - {}'.format(a, b, s)) 
# или print(f'{a} - {b} - {s}')