# Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.
my_f = open('./files/text1.txt', 'w', encoding='utf-8')
content = input('Введите строку \n')
while content != '':
    my_f.writelines(content + '\n')
    content = input('Введите строку \n')

my_f.close()
my_f = open('./files/text1.txt', 'r', encoding='utf-8')
content = my_f.readlines()
print(content)
my_f.close()
