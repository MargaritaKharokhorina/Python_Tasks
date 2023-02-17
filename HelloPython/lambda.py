#калькулятор
def calk1(a,b):
    return a+b

def calc2(a,b):
    return a*b

def math(op, x, y):       
    print(op(x, y))

math(calc2, 5, 10)  #передаем в ф-цию math ф-цию calc2, т.е. наша переменна op 
                    #имеет ссылку на ф-цию calc2 (5*10 == 50)

#реализация через lambda-функцию (имеет произвольное число аргументов 
#и возвращает значение одного выражения):
#calc1 = lambda a,b: a+b
#описание этой ф-ции при вызове math:
math(lambda a,b: a+b, 5, 10)

#Задача: в списке хранятся числа. Нужно выбрать только четные числа и составить
#список пар (число; квадрат числа). С помощью lambda.
#data = [1, 2, 3, 5, 8, 15, 23, 38]
#res = list()

#for i in data:
    #if i % 2 == 0:
        #res.append((i, i**2))
#print(res)

def select(f, col):            #передаем ф-цию и значение (col)
    return [f(x) for x in col] #будет возвращать список, в кот-м к каждому элементу применятся f(x),
                               #проходясь по всем элементам

def where(f, col):
    return[x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)  #2, 8, 38

res = list(select(lambda x: (x, x**2), res))  #возвращаем кортеж - х и х в квадрате
print(res)
#итог сокращенного кода с помощью map и filter в filter.py

