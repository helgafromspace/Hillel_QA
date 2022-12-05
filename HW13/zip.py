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

from typing import Iterable, List, Tuple

# на 2 последовательности

# def custom_zip(*sequences: Iterable, full=False, default=None) -> List[Tuple]:
#     result = []
#     long_seq = max(sequences, key=len)
#     short_seq = min(sequences, key=len)
#     if full:
#         for i in range(len(long_seq)):
#             if i < len(short_seq):
#                 result.append((long_seq[i], short_seq[i]))
#             else:
#                 result.append((long_seq[i], default))
#     else:
#         for i in range(len(short_seq)):
#             result.append((long_seq[i], short_seq[i]))
#     return result

# больше чем на 2
def custom_zip(*args: Iterable, full=False, default=None) -> List[Tuple] :
    min_seq = min (args, key=len)
    result = [[x] for x in args[0]]
    for i in range (1, len (args)) :
        for j in range (len(result)):
            if j < len(args[i]):
                result[j].append(args[i][j])
            else:
                result[j].append(default)
    if full:
        return [tuple(i) for i in result]
    else:
        return [tuple(i) for i in result[:len(min_seq)]]
print(custom_zip(seq1, seq2, seq3))
print(custom_zip(seq1, seq2, full=False))
print(custom_zip(seq1, seq2,seq3, full=True, default="Q"))
print(custom_zip(seq1, seq2, full=True))