#Пользователь вводит время в секундах
sec = int(input('Введите время в секундах'))
#Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс
t_h = sec//3600
t_min = (sec % 3600)//60
t_sec = (sec % 3600) % 60
if t_min < 10:
    mm = ('0' + str(t_min))
else:
    mm = t_min

if t_sec < 10:
    ss = ('0' + str(t_sec))
else:
    ss = t_sec

if t_h > 23:
    print('Введенное количество секунд превышает допустимое количество секунд в сутках')
else:
    print(f'Время в формате чч:мм:сс =  {t_h}:{mm}:{ss}')
