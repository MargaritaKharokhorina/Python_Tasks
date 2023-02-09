#Последовательностью Фибоначчи называется
#последовательность чисел a0, a1, ..., an, ..., где
#a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
#Требуется найти N-е число Фибоначчи

n = int(input('Введите число: '))

def fib_numb(n):
    if n == 0 or n == 1:       
        return n
    else:
        return fib_numb(n - 1) + fib_numb(n - 2)
print(fib_numb(n))
         