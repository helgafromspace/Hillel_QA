#2. Написать функцию, которая возвращает список результатов выполнения заданной функции,
# к соответствующим элементам переданных итерируемых объектов.

#Если переданные итерируемые объекты разной длины, то результат сформировать по кратчайшему итерируемому объекту.
#custom_map(sum, [1, 2, 3], [3, 5, 0, 5]) -> [4, 7, 3]

from typing import Callable, Iterable

def sum(*args):
    result = []
    for i in zip(*args):
        sum = 0
        for j in i:
            sum += j
        result.append(sum)
    return result

def custom_map(function: Callable, *args: Iterable) -> Iterable:
    result = function(*args)
    return result

print(custom_map(sum, [1, 2, 3], [3, 5, 0, 5]))
print(custom_map(sum, [1, 2, 3], [3, 5, 0, 5], [1, 1, 1]))