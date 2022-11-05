# Задание 1: Запросить у пользователя 5 чисел и записать их в список
# my_list = []
# for _ in range(5):
#     my_list.append(int(input('Enter a number: ')))
# print(my_list)

# Задание 2: Дан список A = [1, 2, 3, 4, 5]. Удалить последнее число из списка

# A = [1, 2, 3, 4, 5]
# A.pop()
# print(A)

# Задание 3:Запросить у пользователя 10 чисел и записать их в список A
# Запросить у пользователя число N
# Вывести пользователю сколько в списке A повторяется число N

# A = []
# for _ in range(10):
#     A.append(int(input(f'Enter a number {_+1}/10: ')))
# N = int(input('Enter number you want to count: '))
# print(f'Number {N} repeats {A.count(N)} times')

# Задание 4:
# Запросить у пользователя число N
# Запросить у пользователя N чисел и записать их в список A
# Вывести список в обратной последовательности

# N = int(input('Enter number of list items: '))
# A = []
# for _ in range(N):
#     A.append(int(input('Enter a number: ')))
# print(A[::-1])

# Задание 5:
# Запросить у пользователя 5 чисел и записать их в список A
# Записать все числа из списка A которые больше 5 в список C

# A = []
# for _ in range(5):
#     A.append(int(input('Enter a number: ')))
# C = [i for i in A if i > 5]
# print(C)

# Задание 6:
# Запросить у пользователя число N
# Запросить у пользователя N целых чисел и записать их в список A
# Найти в нем минимальное и максимальное число с помощью цикла (запрещено использовать функцию min, max, sorted, sort). Вывести эти числа.

# N = int(input('Enter number of list items: '))
# A = []
# for _ in range(N):
#     num = int(input('Enter a number: '))
#     A.append(num)
# maximum = A[0]
# minimum = A[0]
# for i in range(len(A)):
#     if A[i] >= maximum:
#         maximum = A[i]
#     if A[i] <= minimum:
#         minimum = A[i]
#
# print(A)
# print(maximum)
# print(minimum)

#Задание 7: Пользователь вводит текст нужно вывести количество чисел в этом тексте
#
# Пример:
# > 'Lorem 222 ipsum, 123 dolor 1 sit amet
# Количество чисел: 3


# text = input('Еnter text: ')
# for i in text:
#     if not i.isdigit():
#         text = text.replace(i,' ')
# text_list = [i for i in text.split(' ') if i.isdigit()]
# print(f'Количество чисел: {len(text_list)}')