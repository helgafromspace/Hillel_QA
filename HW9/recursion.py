# Написать функцию которая принимает целое число - number. Функция должна возвращать 'yes' если number является степенью двойки, иначе 'no'.
# Запрещено пользоваться функцией или оператором возведение в степень.
# Пример:
# is_power_of_two(256) # 'yes' потому что 2 в 8 степени это 256
# is_power_of_two(125) # 'no' потому что это не степень двойки
from typing import Union


def is_power_of_two(n: Union[int, float]) -> Union[float, int]:
    n = n / 2
    if n == 2 or n == 1:  # базовый случай - 2 в первой степени или 2 в 0 степени
        print('yes')
    elif n > 2:
        return is_power_of_two(n)
    else:
        print('no')


is_power_of_two(2)
is_power_of_two(2.0)
is_power_of_two(256)
is_power_of_two(125)
is_power_of_two(0)
is_power_of_two(128)
is_power_of_two(-128)
