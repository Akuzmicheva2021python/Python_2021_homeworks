"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*n_numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    list_of_q = [ i*i for i in n_numbers if type(i) == int]
    return list_of_q



# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(list_of_num,argfilter=ODD):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    list_of_num2=[]
    if argfilter==ODD:
        list_of_num2 = [y for y in list_of_num if type(y) == int and y%2 != 0]
    if argfilter==EVEN:
        list_of_num2 = [y for y in list_of_num if type(y) == int and y%2 == 0]
    if argfilter==PRIME:
        def is_prime(num):
            n = num
            col_dev = 0
            if n == 1:
                return 0
            for i in range(1, n + 1):
                if n % i == 0:
                    col_dev += 1
            return 1 if col_dev==2 else 0
        list_of_num2 =[y for y in list_of_num if type(y) == int and is_prime(y) == 1]
    return list_of_num2

l=filter_numbers([1,2,33,75,19],PRIME)
print(l)
