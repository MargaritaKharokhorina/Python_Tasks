#Ф-ция filter() принимает два арг-та: передаваемую ф-цию и объект.
#Возвращает только те элементы объекта, для кот-х вызов фу-ции (кот.передали) вернул True.

data = [15, 65, 9, 36, 175]
res = list(filter(lambda x: x % 10 == 5, data))  #выведем только те эл-ты, кот.оканчиваются на 5  
print(res)                                       #[15, 65, 175]

#Сократим код из lambda.py и map.py с помощью filter (заменим def where):

#def where/filter(f, col):
    #return[x for x in col if f(x)]
data = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, data)
res = filter(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x**2), res))  #возвращаем кортеж - х и х в квадрате
print(res)

