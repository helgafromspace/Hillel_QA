"""
1. Написать функцию, которая генерируют в директории `directory` `number_of_files` файлов.

Содержимое файлов должно быть случайным, состоять из больших/маленьких латинских букв, цифр и символов пунктуации.

Файл должен содержать случайное число символов в диапазоне от `size/2` до `size` символов.

def file_generator(directory, number_of_files, size)

"""
from random import randint
import string
import os
import threading
import math
import time


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
# file_generator('files',10,20)


#ASCII solution

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

"""
2. Написать функцию (обычную, однопоточную), которая возвращает число букв `letter_to_find` во всех файлах директории `directory`

def letter_counter_in_one_thread(directory, letter_to_find)
"""
#
def letter_counter_in_one_thread(directory, letter_to_find):
    files_list = os.listdir(directory)
    result = 0
    for i in files_list:
        f = open(f'{directory}/{i}', 'r')
        text = f.read()
        if letter_to_find in text:
            result += len(text)
    return result

print(f"letter_counter_in_one_thread result: {letter_counter_in_one_thread('files','g')}")



# def letter_counter_in_one_thread(directory, letter_to_find, output={}):
#     files_list = sorted(os.listdir(directory))
#     result = 0
#     for i in files_list:
#         f = open(f'{directory}/{i}', 'r')
#         text = f.read()
#         if letter_to_find in text:
#             result += len(text)
#     output['value'] = result
#     return output['value']
#
# print(f"letter_counter_in_one_thread result: {letter_counter_in_one_thread('files','g')}")

"""
3. Написать функцию, которая возвращает число букв `letter_to_find` во всех файлах директории `directory`

Функция должна разбить файлы в директории на `number_of_threads` групп, и чтение/подсчет буквы для каждой группы вести в отдельном потоке.

Группы стоит разбить максимально равно.

def letter_counter_in_n_threads(directory, letter_to_find, number_of_threads)

"""
def letter_counter_in_thread_for_group(directory,group, letter_to_find, output ={}):
    result = 0
    for file in group:
        f = open(f'{directory}/{file}', 'r')
        text = f.read()
        if letter_to_find in text:
            result += len(text)
    output['value'] = result
    return output['value']

#
def letter_counter_in_n_threads(directory, number_of_threads, letter_to_find, output=0):
    files_list = os.listdir(directory)
    num_of_files = math.ceil(int(len(files_list)/number_of_threads))
    groups = []
    for i in range(number_of_threads):
        groups.append(files_list[:num_of_files])
        files_list = files_list[num_of_files:]
    thread = [None] * number_of_threads
    output_one = {}
    for i,group in enumerate(groups):
        thread[i]=threading.Thread(target=letter_counter_in_thread_for_group,args = (directory,group,letter_to_find,output_one))
        thread[i].start()
        thread[i].join ()
        output += output_one['value']
    return output

print(f"letter_counter_in_n_threads result: {letter_counter_in_n_threads('files',5,'g')}")



"""
4. Написать клиентский код, который создает файлы, подсичтывает количество букв функцией в одном потоке и в нескольких потоках,
 и выводит время выполнения функций.

"""
