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


def file_generator(directory,number_of_files,size):
    parent_dir = os.path.split(__file__)[0]
    path = os.path.join (parent_dir, directory)
    os.mkdir(path)
    seq = string.digits + string.punctuation + string.ascii_letters
    for i in range(1,number_of_files+1):
        f = open(f'{directory}/file{i}.py','a')
        rand_num = randint(size//2,size)
        rand_string = ''.join([seq[randint(0,len(seq)-1)] for i in range(rand_num)])
        f.write(rand_string)
        f.close()

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
        for letter in text:
            if letter_to_find == letter:
                result += 1
        f.close()
    return result



# def letter_counter_in_one_thread2(directory, letter_to_find, output={}):
#     files_list = sorted(os.listdir(directory))
#     result = 0
#     for i in files_list:
#         f = open(f'{directory}/{i}', 'r')
#         text = f.read()
#         if letter_to_find in text:
#             result += len(text)
#     output['value'] = result
#     return output['value']


"""
3. Написать функцию, которая возвращает число букв `letter_to_find` во всех файлах директории `directory`

Функция должна разбить файлы в директории на `number_of_threads` групп, и чтение/подсчет буквы для каждой группы вести в отдельном потоке.

Группы стоит разбить максимально равно.

def letter_counter_in_n_threads(directory, letter_to_find, number_of_threads)

"""
def letter_counter_in_thread_for_group(directory,group, letter_to_find, index=1,output ={}):
    result = 0
    for file in group:
        f = open(f'{directory}/{file}', 'r')
        text = f.read()
        for letter in text:
            if letter_to_find == letter:
                result += 1
        f.close()
    output[index] = result
    return output[index]

#
def letter_counter_in_n_threads(directory, number_of_threads, letter_to_find, output=0):
    files_list = os.listdir(directory)
    num_of_files = math.ceil(int(len(files_list)/number_of_threads))
    groups = ()
    for i in range(number_of_threads):
        groups += (files_list[:num_of_files],)
        files_list = files_list[num_of_files:]
    thread = [None] * number_of_threads
    output = [{}] * number_of_threads
    output_one = {}
    for i,group in enumerate(groups):
        thread[i]=threading.Thread(target=letter_counter_in_thread_for_group,args = (directory,group,letter_to_find,i,output))
        thread[i].start()
    for i in range(len(thread)):
        thread[i].join()
    return sum(output)



"""
4. Написать клиентский код, который создает файлы, подсичтывает количество букв функцией в одном потоке и в нескольких потоках,
 и выводит время выполнения функций.

"""


files_directory = 'files'
letter = 'g'
number_of_threads = 5

start_time = time.perf_counter()
file_generator(files_directory,11,20)
end_time = time.perf_counter()
print(f'Function file_generator executed in {end_time-start_time} s')

start_time = time.perf_counter()
result_in_one_thread = letter_counter_in_one_thread(files_directory,letter)
end_time = time.perf_counter()
print(f"letter_counter_in_one_thread result: {result_in_one_thread}")
print(f'Function letter_counter_in_one_thread executed in {end_time-start_time} s')

start_time = time.perf_counter()
result_in_n_threads = letter_counter_in_n_threads(files_directory,number_of_threads,letter)
end_time = time.perf_counter()
print(f"letter_counter_in_n_threads result: {result_in_n_threads}")
print(f'Function letter_counter_in_n_threads executed in {end_time-start_time} s')
