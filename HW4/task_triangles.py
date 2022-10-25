#Запросить у пользователя число N - ширина треугольника.


#Вывести треугольник #1 с шириной N с помощью цикла while

N = int(input('Enter triangle width: '))
i = N

while i > 0:
    print('*' * i)
    i -= 1

# #Вывести треугольник #2 с шириной N с помощью цикла while

N = int(input('Enter triangle width: '))
i = 1

while i <= N:
    print('*' * i)
    i += 1

# Вывести треугольник #3 с шириной N с помощью цикла while

N = int(input('Enter triangle width: '))
i = N

while i > 0:
    print(' '*(N-i) + '*' * i)
    i -= 1

# Вывести треугольник #3 с шириной N с помощью цикла while

N = int(input('Enter triangle width: '))
i = 1

while i <= N:
    print(' '*(N-i) + '*' * i)
    i += 1
