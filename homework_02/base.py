from abc import ABC

from homework_02.exceptions import LowFuelError, NotEnoughFuel



class Vehicle(ABC):
    """ Класс ТС (транспортное средство) с запасом топлива


        """

    def __init__(self, weight=0, fuel=0.0, fuel_consumption=1.0, started=False):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started

    def start(self):
        """ метод start, который,
        если ещё не состояние started, проверяет, что топлива больше нуля,
        и обновляет состояние started, иначе выкидывает исключение exceptions.LowFuelError

        """
        if self.started == False:
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
        if  max_distance >= distance:
            self.fuel -= distance * self.fuel_consumption
            return True
        else:
            raise NotEnoughFuel('Недостаточно топлива на указанную дистанцию')
