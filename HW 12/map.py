#2. Написать функцию, которая возвращает список результатов выполнения заданной функции,
# к соответствующим элементам переданных итерируемых объектов.

#Если переданные итерируемые объекты разной длины, то результат сформировать по кратчайшему итерируемому объекту.
# sum2 = lambda x, y: x + y
# sum3 = lambda x, y, z: x + y + z

from typing import Callable, Iterable

def custom_map(function: Callable, *args: Iterable) -> Iterable:
    result = []
    for i in zip(*args):
        i = function(i)
        result.append(i)
    return result


# assert custom_map(sum, [[1, 2, 3], [4, 5]]) == [6, 9]
# assert custom_map(len, [[], (2, 4), [1, 3, 5, 7]]) == [0, 2, 4]
# assert custom_map(str, (17, 23)) == ['17', '23']
# assert custom_map(sum2, [1, 2, 3], [3, 5, 0]) == [4, 7, 3]
# assert custom_map(sum2, [1, 2, 3, 4], (3, 4, 4, 4, 4, 4, 44)) == [4, 6, 7, 8]
# assert custom_map(sum3, [1, 1, 1], [4, 5, 6], [0, 5, 2, 1]) == [5, 11, 9]
