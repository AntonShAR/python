#Узнайте у пользователя число n
n = input('Введите число n: ')
#Найдите сумму чисел n + nn + nnn
x = int(n) + int(n + n) + int(n + n + n)
print(f'Число в формате n + nn + nnn = {x}')
