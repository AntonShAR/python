# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.

with open('./files/text3.txt', 'r', encoding='utf-8') as f_obj:
    sal = []
    less = []
    summ = 0
    my_list = f_obj.readlines()
    for i in range(len(my_list)):
        sal = int(my_list[i].split()[1])
        if sal < 20000:
           less.append(my_list[i].split()[0])
        summ += sal
print(f'Оклад меньше 20.000 {less}, средний оклад {summ / len(my_list)}')
f_obj.close()
