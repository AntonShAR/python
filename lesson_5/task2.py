# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

my_f = open('./files/text2.txt', 'r', encoding='utf-8')
content = my_f.readlines()
print(f'Количество строк в файле = {len(content)}')
my_f = open('./files/text2.txt', 'r', encoding='utf-8')
for i in range(len(content)):
    a = content[i].split()
    print(f'Количество слов {i + 1} строки = {len(a)}')
my_f.close()
