# 3. Написать функцию, которая принимает несколько итерируемых объектов,
# и возвращает список из кортежей составленных из элементов итерируемых объектов одного индекса.
#
# Функция также должна принимать параметры с дефолтными значения:
#
# full=False - по умолчанию "склеить" последовательности по кратчайшей, иначе по самой длинной
#
# default=None - если full=True, вместо недостающих элементов поставить значение указанное в параметре default
#
seq1 = [1, 2, 3, 4, 5]
seq2 = [9, 8, 7]
# custom_zip(seq1, seq2) -> [(1, 9), (2, 8), (3, 7)])

#
# custom_zip(seq1, seq2, full=True, default="Q") -> [(1, 9), (2, 8), (3, 7), (4, 'Q'), (5, 'Q')]

from typing import Iterable, List

def custom_zip(*sequences: Iterable, full=False, default=None) -> List[List]:
    if full:
        result = []
        if len(seq1) > len(seq2):
            for i in range(len(seq1)):
                if i < len(seq2):
                    result.append((seq1[i], seq2[i]))
                else:
                    result.append((seq1[i], default))
        else:
            result = list(zip(*sequences))
    else:
        result = list(zip(*sequences))
    return result

print(custom_zip(seq1, seq2))
print(custom_zip(seq1, seq2, full=False))
print(custom_zip(seq1, seq2, full=True, default="Q"))
print(custom_zip(seq1, seq2, full=True))