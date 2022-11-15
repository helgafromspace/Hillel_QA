# 1) Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент. В исходном списке минимум 2 элемента.

# def change(lst):
#     if len(lst) > 1:
#         lst[0], lst[-1] = lst[-1], lst[0]
#         return lst
#     else:
#         return 'List should have at least 2 elements'
# print(change([1,2,3,4,5]))

# 2) Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь, в котором каждый элемент списка является и ключом и значением.
# Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.

# def to_dict(lst):
#     my_dict = {}
#     for i in lst:
#         my_dict[i] = i
#     return my_dict
#
# print(to_dict([1,2,3,4,5]))

# 3) Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start» до величины «end» включительно.
# Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.

# def sum_range(start, end):
#     summa = 0
#     if start > end:
#         start, end = end, start
#     for i in range(start, end + 1):
#         summa += i
#     return summa
#
# print(sum_range(5,20))

#Напишите функцию read_last(lines, file), которая будет открывать определенный файл file
# и выводить на печать построчно последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число).

# def read_last(lines, file):
#     if isinstance(lines, int) and lines > 0:
#         f = open(file, 'r')
#         lst = f.readlines()
#         if len(lst) >= lines:
#             lst = [i.strip() for i in lst[len(lst)-lines::]]
#             print(*lst, sep='\n')
#         else:
#             print('Number of lines to display are bigger than total lines count')
#     else:
#         print('Lines should have integer type and positive value')
#
# read_last(5, 'file.txt')