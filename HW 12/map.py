#2. Написать функцию, которая возвращает список результатов выполнения заданной функции,
# к соответствующим элементам переданных итерируемых объектов.

#Если переданные итерируемые объекты разной длины, то результат сформировать по кратчайшему итерируемому объекту.
#custom_map(sum, [1, 2, 3], [3, 5, 0, 5]) -> [4, 7, 3]

from typing import Callable, Iterable


def sum(*args):
    result = 0
    for i in range(len(args)):
        result += args[i]
    return result

def custom_map(function: Callable, *args: Iterable) -> Iterable:
    result = list(map(function, *args))
    return result

print(custom_map(sum, [1, 2, 3], [3, 5, 0, 5]))
print(custom_map(sum, [1, 2, 3], [3, 5, 0, 5], [5, 6, 8], [1, 1]))