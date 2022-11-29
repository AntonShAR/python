# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict
list1 = ['winter', 'spring', 'summer', 'autumn']
dict1 = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
month = int(input('Введите номер месяца: '))
if month == 12 or month == 1 or month == 2:
    print(f'Решение с помощью списка: {list1[0]}')
    print(f'Решение с помощью словаря: {dict1.get(1)}')
elif month == 3 or month == 4 or month == 5:
    print(f'Решение с помощью списка: {list1[1]}')
    print(f'Решение с помощью словаря: {dict1.get(2)}')
elif month == 6 or month == 7 or month == 8:
    print(f'Решение с помощью списка: {list1[2]}')
    print(f'Решение с помощью словаря: {dict1.get(3)}')
elif month == 9 or month == 10 or month == 11:
    print(f'Решение с помощью списка: {list1[3]}')
    print(f'Решение с помощью словаря: {dict1.get(4)}')
else:
    print('Некорректный ввод номера месяца')
