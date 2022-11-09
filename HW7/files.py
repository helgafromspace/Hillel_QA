#Задание 1: Дан файл с произвольным текстом, необходимо найти все числа в файле и записать в список numbers

# f = open('files/text_1_task.txt', 'r')
# data = f.read()
# for i in data:
#     if not i.isdigit():
#         data = data.replace(i, ' ')
# numbers = [i for i in data.split(' ') if i.isdigit()]
# print(numbers)
#
# f.close()

#Задание 2: Запросить у пользователя текст и записать его в файл data.txt

# text = input('Enter your text: ')
# with open('files/data.txt', 'w') as f:
#     f.write(text)
# f.close()

# Задание 3: Запросить у пользователя число N и запросить N чисел у пользователя, потом записать их в файл numbers.txt через пробел

# with open('files/numbers.txt', 'w', encoding = 'utf-8') as f:
#     N = int (input ('Enter number of digits: '))
#     for _ in range(N):
#         num = input(f'Enter digit {_ + 1}: ')
#         f.write(num + ' ')
#
# f.close()

#Задание 4: Сгенерировать 100 рандомных чисел и записать их в файл random_numbers.txt, где одна строка = одно число

# import random
#
# numbers = [str(random.randint(1, 100)) + '\n' for i in range(100)]
#
# with open('files/random_numbers.txt', 'w', encoding = 'utf-8') as f:
#     f.writelines(numbers)
#
# f.close()

#Задание 5: Дан файл с произвольным текстом(whatevertext.txt), нужно найти количество слов в файле и вывести пользователю

# f = open('files/whatevertext.txt', 'r')
# data = f.read()
# for i in data:
#     if not i.isalpha():
#         data = data.replace(i, ' ')
# words_list = [i for i in data.split(' ') if i.isalpha()]
# print(len(words_list))
# f.close()

#Задание 6: Дан файл в котором записаны числа через пробел, необходимо вывести пользователю сумму этих чисел

# f = open('files/numbers_list.txt', 'r')
# data = [int(i) for i in f.read().split(' ')]
# print(sum(data))
# f.close()

# Задание 7:
# Дан файл в котором записан текст, необходимо вывести топ 5 строк которые чаще всего повторяются, пример:
# 'в' - 20 раз
# 'привет' - 10 раз
# 'как' - 9 раз
# 'у' - 7
# 'world' - 4