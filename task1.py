#  Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
#  Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный,
#  желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
#  третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
#  порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
# сообщение и завершать скрипт.

import time


class TrafficLight():

    # Определяем время ожидания сигнала светофора
    red_color_wait = 7
    yellow_color_wait = 2
    green_color_wait = 5

    # Определяем названия цветов сигналов светофора
    red_color_name = 'красный'
    yellow_color_name = 'желтый'
    green_color_name = 'зеленый'


    def __init__(self, color):
        self.__color = color
        print(f'Создан экземпляр класса TrafficLight со стартовым цветом {self.__color}')

    def switch_light(self, color, wait_period):
        print(f'Включен {color} свет, время ожидания {wait_period} сек')
        time.sleep(wait_period)

    def running(self, color):

        # Если при вызове метода цвет не указан, берем из родительского класса
        # В противном случае стартуем с цвета, объявленного при вызове метода
        if not color:
            loc_color = self.__color
        else:
            loc_color = color

        if loc_color == self.red_color_name:
            self.switch_light('красный', self.red_color_wait)
            self.switch_light('желтый', self.yellow_color_wait)
            self.switch_light('зеленый', self.green_color_wait)
        elif loc_color == self.yellow_color_name:
            self.switch_light('желтый', self.yellow_color_wait)
            self.switch_light('зеленый', self.green_color_wait)
        else:
            self.switch_light('зеленый', self.green_color_wait)

color = input('Выберите цвет сигнала - красный, желтый или зеленый')
color = color.lower()
obj1 = TrafficLight(color)
# Работа метода, когда цвет указан
obj1.running(color)

# Работа метода, когда цвет не указан
obj1.running('')
