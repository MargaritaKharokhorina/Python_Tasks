# Если требуется создание какой-то пары:
(a) = (3, 4)
print(a)      # (3, 4)
print (a[0])  # 3
print (a[-1]) # 4

(b) = (8, 5, 6)
for item in b: 
    print(item)

#Кортеж можно распаковать в отдельные переменные:
t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue)) # r:red g:green b:blue

