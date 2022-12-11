# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
summ = 0
my_f = open('./files/text5.txt', 'w', encoding='utf-8')
content = input('Введите набор чисел, разделенных пробелами: ')
my_f.writelines(content)
my_f.close()
my_f = open('./files/text5.txt', 'r', encoding='utf-8')
content = my_f.read().split()
print(content)
print(len(content))
for i in range(len(content)):
    summ += int(content[i])
print(summ)
my_f.close()
