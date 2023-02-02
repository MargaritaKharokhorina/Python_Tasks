def new_string(symbol, count = 3):
    return symbol * count

print(new_string('!', 5))  # !!!!!
print(new_string('!'))     # !!!
print(new_string(4))       # 12

# Возможность передачи любого количества элементов -
# для этого при описании ф-ции перед аргументом ставим "звездочку"
# и далее работаем с аргументом, как с набором:

def concantenatio(*params):
    res: str = ""
    for item in params:
        res+= item
    return res

print(concantenatio('a', 's', 'd', 'w')) # asdw
print(concantenatio('a', '1'))           # a1
#print(concantenatio(1, 2, 3, 4))        # TypeError:...(так как в этом примере используем склеивание строк, а не чисел)
