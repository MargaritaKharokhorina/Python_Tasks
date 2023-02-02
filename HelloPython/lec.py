#with open('file.txt', 'w') as data:
    #data.write('line 1\n')
    #data.write('line 2\n')
   
colors = ['red', 'green', 'blue', 'etc']
data = open('file.txt', 'a')
# data.writelines(colors) # разделителей не будет
data.write('\nLINE 210\n')
data.write('LINE 330\n')
data.close()

# Посмотрим на чтение данных из файла, создадим путь к нашему файлу:
path = 'file.txt'
data = open(path, 'r') # открываем в режиме чтения
for line in data:      # при помощи цикла пройдемся по файлу
    print(line)        # считаем все строки
data.close()           # после чтения разрываем связь файловой переменной с файлом на диске
  
exit()
           


exit()

