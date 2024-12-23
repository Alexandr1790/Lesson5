box = ['apple', 'phone', 'passport']
print(box[2])
box[1]='a pan'
print (box)
box.append('Book') #Добавление элементов в конец списка
print(box)
box.extend('string') # Добавление по одному сисмволу
box.remove('apple') #Удаление элементов
print(box)
print('apple' in box) #Можно проверить находиться ли какой-то элемент в переменной
print('apple' not in box)
print(box[0:2:2]) # Работает так же как и со строками