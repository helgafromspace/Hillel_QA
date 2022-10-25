# Пользователь вводит с клавиатуры три числа в переменные a, b, c. Если все числа больше 10 и первые два числа делятся на 3, то вывести yes, иначе no

# a = int(input('Enter number a: '))
# b = int(input('Enter number b: '))
# c = int(input('Enter number c: '))
#
# if a > 10 and a % 3 == 0 and b > 10 and b % 3 == 0 and c > 10:
#     print('yes')
# else:
#     print('no')

# Задание #2 (-5 баллов):Если все числа будут равны, то код выдаст ошибку
# Пользователь вводит с клавиатуры три числа в переменные a, b, c. Найдите наибольшее число из них и запишите в переменную max.

a = int(input('Enter number a: '))
b = int(input('Enter number b: '))
c = int(input('Enter number c: '))

if (a > b and a > c) or (a > b == c) or (a == b == c):
    max = a
elif (b > a and b > c) or (b > a == c):
    max = b
elif (c > a and c > b) or (c > a == b):
    max = c
print(max)

# Пользователь вводит два числа A и B, нужно вывести сумму всех четных чисел в диапазоне от A до B.

A = int(input('Enter number A: '))
B = int(input('Enter number B: '))
total = 0

if A == B:
    print('A and B should have different values')
else:
    if A > B:
        A, B = B, A
    for i in range(A, B + 1):
        if i % 2 == 0:
            total += i
    print(total)
