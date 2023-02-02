# Если в списках используем в качестве ключа индекс,
# то для словарей указываем то значение ключа,
# которое определили при его описании.

dictionary = {}
# \ для записи с новой строки
dictionary = \
    {'up': '|',                # слева - ключ, справа - значение
    'left': '<--',
    'down': '||',
    'right': '-->'
    }
# print(dictionary)           # {'up': '|', 'left': '<--', 'down': '||', 'right': '-->'}
# print(dictionary['left'])   # <--
# типы ключей могут отличаться

# Можем получить все ключи или все значения:

for k in dictionary.keys():   # это чтобы посмотреть на ключи, а на значения - dictionary.values()
    print(k)                  # или for v in dictionary:
                              # print(dictionary[v]) - тоже для получения значений

#Для замены ключа:
print(dictionary['up'])
dictionary['up'] = 'upward'
print(dictionary['up'])       # upward

  