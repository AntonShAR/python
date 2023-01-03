# Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда,
# которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    def consumption(self):
        return f'Сумма затраченной ткани равна: {self.param * 6.5 + 0.5 + 2 * self.param + 0.3 } см'

    @abstractmethod
    def abstract(self):
        return 'Main abstract metod'


class Coat(Clothes):
    @property
    def cons(self):
        return f'Для пошива пальто нужно: {self.param * 6.5 + 0.5 } см ткани'

    def abstract(self):
        return 'Second abstract metod'


class Costume(Clothes):
    def cons(self):
        return f'Для пошива костюма нужно: {2 * self.param + 0.3 } см ткани'

    def abstract(self):
        pass

coat = Coat(50)
costume = Costume(170)
print(f"Сумма затраченной ткани равна: {coat.param * 6.5 + 0.5 + costume.param * 2 + 0.3} см")
print(costume.cons())
print(coat.cons)
print(coat.abstract())
print(costume.abstract())
