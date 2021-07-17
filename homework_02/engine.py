"""
create dataclass `Engine`
"""
from dataclasses import dataclass

@dataclass
class Engine:
    """ Класс определяющий рабочий объем двигателя и число цилиндров """
    volume: float
    pistons: int
