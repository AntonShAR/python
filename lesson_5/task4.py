# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
replace = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_text = []
with open('./files/text4_in.txt', 'r', encoding="utf-8") as file:
    with open('./files/text4_out.txt', 'w', encoding="utf-8") as new_file:
        my_list = file.readlines()
        for i in my_list:
            i = i.split(' ', 1)
            new_text.append(replace[i[0]] + ' ' + i[1])
        new_file.writelines(new_text)
    new_file.close()
file.close()
