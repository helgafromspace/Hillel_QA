# 3. Написать функцию, которая принимает несколько итерируемых объектов,
# и возвращает список из кортежей составленных из элементов итерируемых объектов одного индекса.
#
# Функция также должна принимать параметры с дефолтными значения:
#
# full=False - по умолчанию "склеить" последовательности по кратчайшей, иначе по самой длинной
#
# default=None - если full=True, вместо недостающих элементов поставить значение указанное в параметре default

# custom_zip(seq1, seq2) -> [(1, 9), (2, 8), (3, 7)])
# custom_zip(seq1, seq2, full=True, default="Q") -> [(1, 9), (2, 8), (3, 7), (4, 'Q'), (5, 'Q')]

seq1 = [1, 2, 3, 4, 5]
seq2 = [9, 8, 7]
seq3 = [5, 5, 2, 1]
seq4 = [6, 6, 8, 9, 7, 5]

from typing import Iterable, List, Tuple

#Смотрел вторую версию незакоменченную. 70 за то что не работает, если переданные списки увеличиваются по длине.
# Правильно будет как и написала определить какая последовательность самая длинная, но не брать ее как базовую (как у тебя реализовано),
# а проходить по всем последовательностям в том порядке в котором они переданы и добавлять свои или дефолтные элементы в зависимости от длины этой последовательности.



def custom_zip(*args: Iterable, full=False, default=None) -> List[Tuple] :
    min_seq = min (args, key=len)
    max_seq = max (args, key=len)
    result = [[x] for x in args[0]]
    for i in range(1, len(args)):
        for j in range(len(result)):
            if j < len(args[i]):
                result[j].append(args[i][j])
            else:
                result[j].append(default)
    if full:
        return [tuple(i) for i in result]
    else:
        return [tuple(i) for i in result[:len(min_seq)]]
print(custom_zip(seq1, seq2, seq3))
print(custom_zip(seq1, seq2, seq3, full=False))
print(custom_zip(seq1, seq2, seq3, seq4, full=True, default="Q"))
print(custom_zip(seq1, seq2, full=True))