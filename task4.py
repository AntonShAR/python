# Пользователь вводит строку из нескольких слов, разделённых пробелами
# Вывести каждое слово с новой строки. Строки нужно пронумеровать
# Если слово длинное, выводить только первые 10 букв в слове
mine_string = input('Введите строку ')
word = []
c = 1
for el in range(0, mine_string.count(' ') + 1):
    word = mine_string.split(' ')
    if len(str(word)) <= 10:
        print(f'{c} {word[el]}')
        c += 1
    else:
        print(f'{c} {word[el] [0:10]}')
        c += 1
