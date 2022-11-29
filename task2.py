# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
my_list_len = int(input('Введите размер массива: '))
my_list = []
for el in range(0, my_list_len):
    my_list.append(input(f'Введите {str(el)} элемент'))
print(my_list)
if my_list_len % 2 == 0:
    my_list_len -= 1
else:
    my_list_len -= 2
for el in range(0, my_list_len):
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]

print(my_list)
