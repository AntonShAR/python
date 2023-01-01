#  Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title: str):
        self.title = title
    def draw(self):
        print(f'Рисуем с помощью принадлежности {self.title}')

class Pen(Stationery):
    def draw(self):
        print(f'Зарисовка с помощью принадлежности {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Прорисовка с помощью принадлежности {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Отрисовка с помощью принадлежности {self.title}')

stationery = Stationery('уголёк')
stationery.draw()

pen = Pen('шариковая ручка')
pen.draw()

pencil = Pencil('простой карандаш')
pencil.draw()

handle = Handle('перманентный маркер')
handle.draw()
