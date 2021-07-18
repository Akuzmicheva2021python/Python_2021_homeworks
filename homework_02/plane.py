"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import *
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo = 100

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, dobcargo: int):
        """
        метод load_cargo, который принимает число, проверяет,
        что в сумме с текущим cargo не будет перегруза, и обновляет значение,
        в ином случае выкидывает исключение exceptions.CargoOverload
        """
        if self.max_cargo >= self.cargo + dobcargo:
            self.cargo += dobcargo
        else:
            raise CargoOverload("Перегрузка!")

    def remove_all_cargo(self):
        """
        метод remove_all_cargo, который обнуляет значение cargo и
        возвращает значение cargo, которое было до обнуления
        """
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo
