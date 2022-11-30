# Реализовать функцию my_func(), которая принимает три
# позиционных аргумента и возвращает сумму наибольших двух аргументов.
def my_func(arg1, arg2, arg3):
    return arg1 + arg2 + arg3 - min(arg1, arg2, arg3)

a1 = int(input('Введите 1 аргумент: '))
a2 = int(input('Введите 2 аргумент: '))
a3 = int(input('Введите 3 аргумент: '))
print(my_func(a1, a2, a3))
