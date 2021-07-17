"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import *
from homework_02.engine import *

class Car(Vehicle):
    """ Класс Авто """
    engine = Engine(None, None)
    #def __init__(self, weight=0, started=False, fuel=0.0, fuel_consumption=1.0, engine = None):
    #    super().__init__(weight, started, fuel, fuel_consumption)
    #    self.engine = engine

    def set_engine(self, x:Engine):
        """
        метод set_engine,
        который принимает в себя экземпляр объекта Engine и устанавливает на текущий экземпляр Car
        """
        if isinstance(x, Engine):
            self.engine = x
