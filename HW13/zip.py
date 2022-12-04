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

from typing import Iterable, List

def custom_zip(*sequences: Iterable, full=False, default=None) -> List[List]:
    result = []
    long_seq = max(seq1, seq2, key=len)
    short_seq = min(seq1, seq2, key=len)
    if full:
        for i in range(len(long_seq)):
            if i < len(short_seq):
                result.append((long_seq[i], short_seq[i]))
            else:
                result.append((long_seq[i], default))
    else:
        for i in range(len(short_seq)):
            result.append((long_seq[i], short_seq[i]))
    return result

print(custom_zip(seq1, seq2))
print(custom_zip(seq1, seq2, full=False))
print(custom_zip(seq1, seq2, full=True, default="Q"))
print(custom_zip(seq1, seq2, full=True))