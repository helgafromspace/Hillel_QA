"""
1. Написать функцию, которая генерируют в директории `directory` `number_of_files` файлов.

Содержимое файлов должно быть случайным, состоять из больших/маленьких латинских букв, цифр и символов пунктуации.

Файл должен содержать случайное число символов в диапазоне от `size/2` до `size` символов.

def file_generator(directory, number_of_files, size)

"""
from random import randint
import string
import os

# def file_generator(directory,number_of_files,size):
#     parent_dir = os.path.split(__file__)[0]
#     path = os.path.join (parent_dir, directory)
#     os.mkdir(path)
#     for i in range(1,number_of_files+1):
#         f = open(f'{directory}/file{i}.py','a')
#         rand_num = randint(size/2,size)
#         for _ in range(rand_num):
#             f.write(f'{chr(randint(33,126))}')
#
# file_generator('files',3,10)

# def file_generator(directory,number_of_files,size):
#     parent_dir = os.path.split(__file__)[0]
#     path = os.path.join (parent_dir, directory)
#     os.mkdir(path)
#     seq = string.digits + string.punctuation + string.ascii_letters
#     for i in range(1,number_of_files+1):
#         f = open(f'{directory}/file{i}.py','a')
#         rand_num = randint(size/2,size)
#         for _ in range(rand_num):
#             f.write(f'{seq[randint(0,len(seq)-1)]}')
#
# file_generator('files',3,10)

"""
2. Написать функцию (обычную, однопоточную), которая возвращает число букв `letter_to_find` во всех файлах директории `directory`

def letter_counter_in_one_thread(directory, letter_to_find)
"""

# def letter_counter_in_one_thread(directory, letter_to_find=0):
#     files_list = os.listdir(directory)
#     for i in files_list:
#         f = open(f'{directory}/{i}', 'r')
#         text = f.read()
#         letter_to_find += len(text)
#     return letter_to_find
#
# print(letter_counter_in_one_thread('files'))

"""
3. Написать функцию, которая возвращает число букв `letter_to_find` во всех файлах директории `directory`

Функция должна разбить файлы в директории на `number_of_threads` групп, и чтение/подсчет буквы для каждой группы вести в отдельном потоке.

Группы стоит разбить максимально равно.

def letter_counter_in_n_threads(directory, letter_to_find, number_of_threads)
"""

"""
4. Написать клиентский код, который создает файлы, подсичтывает количество букв функцией в одном потоке и в нескольких потоках,
 и выводит время выполнения функций.

"""