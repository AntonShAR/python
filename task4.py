# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.

class Car:
    def __init__(self, color: str, name: str, is_police: bool):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f'Разгоняемся до {speed} км/ч')

    def stop(self):
        self.speed = 0
        print('Стоп')

    def turn(self, direction: str):
        if self.speed > 0:
            print(f'Поворачиваем {direction}')
        else:
            print('Не можем повернуть - стоим')

    def show_speed(self):
        print(f'Скорость {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print(f'Внимание! Превышение скорости {self.speed} км/ч')
        else:
            print(f'Скорость {self.speed} км/ч')


class SportCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False


class WorkCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print(f'Внимание! Превышение скорости {self.speed} км/ч')
        else:
            print(f'Скорость {self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = True


def test_drive(vehicle):
    print(f"Тест-драйв {'полицейского' if vehicle.is_police else 'гражданского'} автомобиля {vehicle.name}, цвет {vehicle.color}")
    vehicle.go(40)
    vehicle.show_speed()
    vehicle.turn('направо')
    vehicle.stop()
    vehicle.show_speed()
    vehicle.turn('налево')
    vehicle.go(60)
    vehicle.show_speed()
    vehicle.go(120)
    vehicle.show_speed()
    vehicle.stop()
    print("\n\n")

print('Номера классов автомобилей: 1 - обычный, 2 - городской, 3 - спортивный, 4 - рабочий, 5 - полицейский')
a = input('Введите номер класса машины')
car_color = input('Введите цвет')
car_mark = input('Введите марку')
match a.split():
    case ['1']:
        police = bool(input('Машина является полицейской? 1 - да, 0 - нет'))
        obj = Car(car_color, car_mark, police)
        test_drive(obj)
    case ['2']:
        obj = TownCar(car_color, car_mark)
        test_drive(obj)
    case ['3']:
        obj = TownCar(car_color, car_mark)
        test_drive(obj)
    case ['4']:
        obj = TownCar(car_color, car_mark)
        test_drive(obj)
    case ['5']:
        obj = TownCar(car_color, car_mark)
        test_drive(obj)
    case _: print('Введен некорректный класс автомобиля')
