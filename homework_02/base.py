from abc import ABC

from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    """ Класс ТС (транспортное средство) с запасом топлива
    атрибуты weight, started, fuel, fuel_consumption со значениями по умолчанию
        """
    weight = 100
    started = False
    fuel = 0
    fuel_consumption = 1.0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        """ метод start, который,
        если ещё не состояние started, проверяет, что топлива больше нуля,
        и обновляет состояние started, иначе выкидывает исключение exceptions.LowFuelError

        """
        if self.started is False:
            if self.fuel > 0:
                self.started = True
                print('На старт!')
                return self.started
            else:
                raise LowFuelError('Нет топлива. Старт невозможен.')

    def move(self, distance):
        """ метод move, который проверяет, что достаточно топлива для преодоления переданной дистанции,
        и изменяет количество оставшегося топлива,
        иначе выкидывает исключение exceptions.NotEnoughFuel
        """

        max_distance = self.fuel/self.fuel_consumption
        if max_distance >= distance:
            self.fuel -= distance * self.fuel_consumption
            return True
        else:
            raise NotEnoughFuel('Недостаточно топлива на указанную дистанцию')
