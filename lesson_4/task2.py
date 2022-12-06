# Представлен список чисел. Необходимо вывести элементы исходного списка, значения
# которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для его формирования используйте генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_lst = []
generator = (el for el in range(1, len(lst)))
for el in generator:
    if lst[el] > lst[el - 1]:
        result_lst.append(lst[el])
print(f'Исходый список: {lst}')
print(f'Список элементов, удовлетворяющих условию: {result_lst}')
