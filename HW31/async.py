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

def file_generator(directory,number_of_files,size):
    parent_dir = os.path.split(__file__)[0]
    path = os.path.join (parent_dir, directory)
    os.mkdir(path)
    seq = string.digits + string.punctuation + string.ascii_letters
    for i in range(1,number_of_files+1):
        f = open(f'{directory}/file{i}.py','a')
        rand_num = randint(size/2,size)
        for _ in range(rand_num):
            f.write(f'{seq[randint(0,len(seq)-1)]}')

file_generator('files',10,20)


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
# def letter_counter_in_one_thread(directory, letter_to_find=0):
#     files_list = os.listdir(directory)
#     for i in files_list:
#         f = open(f'{directory}/{i}', 'r')
#         text = f.read()
#         letter_to_find += len(text)
#     return letter_to_find
#
# print(letter_counter_in_one_thread('files'))

def letter_counter_in_one_thread(directory, letter_to_find={}):
    files_list = sorted(os.listdir(directory))
    result = 0
    for i in files_list:
        f = open(f'{directory}/{i}', 'r')
        text = f.read()
        result+= len(text)
    letter_to_find['value'] = result
    return letter_to_find['value']

print(f"letter_counter_in_one_thread result: {letter_counter_in_one_thread('files')}")

"""
3. Написать функцию, которая возвращает число букв `letter_to_find` во всех файлах директории `directory`

Функция должна разбить файлы в директории на `number_of_threads` групп, и чтение/подсчет буквы для каждой группы вести в отдельном потоке.

Группы стоит разбить максимально равно.

def letter_counter_in_n_threads(directory, letter_to_find, number_of_threads)

"""

#
import shutil
def dir_segregation(parent_dir,sub_dir, num_of_files):
    root = os.path.split(__file__)[0]
    files_list = os.listdir(parent_dir)
    dir_start_path = os.path.join (root, f'{parent_dir}')
    dir_end_path = os.path.join (root, f'{parent_dir}/{sub_dir}')
    num_of_dirs = int(len(files_list)/num_of_files)
    index = 0
    for i in range(1,num_of_dirs+1):
        dir_end_path_local = os.path.join (root, f'{dir_end_path}{i}')
        os.mkdir(dir_end_path_local)
        for k in range (1, num_of_files + 1):
            file_start_path = f'{dir_start_path}/file{k+index}.py'
            file_end_path = f'{dir_end_path_local}/file{k+index}.py'
            shutil.move (file_start_path, file_end_path)
        index += num_of_files

# dir_segregation('files','sub_dir',5)
#
def letter_counter_in_n_threads(directory, number_of_threads, letter_to_find=0):
    """ function works ok if (number_of_files / number_of_threads) % 2 == 0 """
    files_list = os.listdir(directory)
    num_of_files = math.ceil(int(len(files_list)/number_of_threads))
    dir_segregation ('files', 'sub_dir', num_of_files)
    dir_list = sorted(os.listdir(directory))
    thread = [None] * number_of_threads
    letter_to_find_one = {}
    for i,sub_dir in enumerate(dir_list):
        thread[i]=threading.Thread(target=letter_counter_in_one_thread,args = (f'{directory}/{sub_dir}',letter_to_find_one))
        thread[i].start()
        thread[i].join ()
        letter_to_find += letter_to_find_one['value']
    return letter_to_find

print(f"letter_counter_in_n_threads result: {letter_counter_in_n_threads('files',5)}")



"""
4. Написать клиентский код, который создает файлы, подсичтывает количество букв функцией в одном потоке и в нескольких потоках,
 и выводит время выполнения функций.

"""
