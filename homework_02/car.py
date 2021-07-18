"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import *
from homework_02.engine import *


class Car(Vehicle):
    """ Класс Авто """
    engine = Engine(None, None)

    def __init__(self, weight, fuel, fuel_consumption):
        super().__init__(weight, fuel, fuel_consumption)
    #    self.engine = engine

    def set_engine(self, x: Engine):
        """
        метод set_engine,
        который принимает в себя экземпляр объекта Engine и устанавливает на текущий экземпляр Car
        """
        if isinstance(x, Engine):
            self.engine = x
