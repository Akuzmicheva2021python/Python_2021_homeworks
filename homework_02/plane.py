"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import *
from homework_02.exceptions import CargoOverload

class Plane(Vehicle):

    def __init__(self, max_cargo , weight, fuel, fuel_consumption, started=False):
        super().__init__(weight, fuel, fuel_consumption, started)
        self.cargo = 0
        self.max_cargo = max_cargo
        # self.weight = max_cargo
        # self.weight = weight + max_cargo


    def load_cargo(self, y: int):
        """
        метод load_cargo, который принимает число, проверяет,
        что в сумме с текущим cargo не будет перегруза, и обновляет значение,
        в ином случае выкидывает исключение exceptions.CargoOverload
        """
        if self.max_cargo >= self.cargo + y:
            self.cargo += y
        else:
            raise CargoOverload("Перегрузка!")


    def remove_all_cargo(self):
        """
        метод remove_all_cargo, который обнуляет значение cargo и возвращает значение cargo, которое было до обнуления
        """
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo

