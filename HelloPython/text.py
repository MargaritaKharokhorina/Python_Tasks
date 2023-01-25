# О работе со строками str

text = 'съешь еще этих мягких французских булок'

print(text)                 # print(text[:])
print(len(text))            # ф-ция предоставляет количество символов -> 39
print('еще' in text)        # True
print(text.isdigit())       # False
print(text.islower())       # True
print(text.replace('еще', 'ЕЩЕ'))

# Срезы при работе со строками

print(text[0])
# print(text[len(text)])    #IndexError
print(text[len(text)-1])    #к
print(text[-5])             #б
print(text[2:5])            #cъ
print(text[len(text)-2:])   #ок
print(text[2:9])            #ешь еще
print(text[6:-18])          #еще этих мягких
print(text[::6])            #сеикакл print(text[0:len(text):6])
text = text[2:9] + text[-5] + text[:2]
print(text)
