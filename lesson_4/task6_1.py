# итератор, генерирующий целые числа, начиная с указанного;
# Подсказка: используйте функцию count() и cycle() модуля itertools.
# Например, в первом задании выводим целые числа,начиная с 3.
# При достижении числа 10 — завершаем цикл.
from itertools import count

def number_gen(start_number):
    for el in count(start_number):
        yield el


for i in number_gen(start_number=3):
    print(i)
    if i >= 10:
        break
