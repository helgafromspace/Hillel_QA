# 2. Написать функцию, которая возвращает список результатов выполнения заданной функции,
# к соответствующим элементам переданных итерируемых объектов.

# Если переданные итерируемые объекты разной длины, то результат сформировать по кратчайшему итерируемому объекту.
sum2 = lambda x, y : x + y
sum3 = lambda x, y, z : x + y + z

from typing import Callable, Iterable


# def custom_map(function: Callable, *args: Iterable) -> Iterable :
#     result = []
#     count = 0
#     for arg in args:
#         count += 1
#     if count == 1:
#         for arg in args:
#             for i in arg:
#                 result.append(function(i))
#     else:
#         for arg in zip(*args):
#             result.append(function(*arg))

#     return result


def custom_map(function: Callable, *args: Iterable) -> Iterable :
    result = []
    count = len(args)
    # count = 0
    # for arg in args:
    #     count += 1
    if count == 1:
        # for arg in args:
        #     for i in arg:
        #         result.append(function(i))
        for i in args[0]:
            result.append(function(i))
    else:
        for arg in zip(*args):
            result.append(function(*arg))

    return result



assert custom_map(sum, [[1, 2, 3], [4, 5]]) == [6, 9]
assert custom_map(len, [[], (2, 4), [1, 3, 5, 7]]) == [0, 2, 4]
assert custom_map(str, (17, 23)) == ['17', '23']
assert custom_map(sum2, [1, 2, 3], [3, 5, 0]) == [4, 7, 3]
assert custom_map(sum2, [1, 2, 3, 4], (3, 4, 4, 4, 4, 4, 44)) == [4, 6, 7, 8]
assert custom_map(sum3, [1, 1, 1], [4, 5, 6], [0, 5, 2, 1]) == [5, 11, 9]

print(custom_map(sum, [[1, 2, 3], [4, 5]]))
print(custom_map(len, [[], (2, 4), [1, 3, 5, 7]]))
print(custom_map(str, (17, 23)))
print (custom_map (sum2, [1, 2, 3], [3, 5, 0]))
print(custom_map(sum2, [1, 2, 3, 4], (3, 4, 4, 4, 4, 4, 44)))
print(custom_map(sum3, [1, 1, 1], [4, 5, 6], [0, 5, 2, 1]))
