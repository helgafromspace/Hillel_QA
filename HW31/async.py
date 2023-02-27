"""
1. Написать функцию, которая генерируют в директории `directory` `number_of_files` файлов.

Содержимое файлов должно быть случайным, состоять из больших/маленьких латинских букв, цифр и символов пунктуации.

Файл должен содержать случайное число символов в диапазоне от `size/2` до `size` символов.

def file_generator(directory, number_of_files, size)

"""
from random import randint
import os

def file_generator(directory,number_of_files,size):
    parent_dir = os.path.split(__file__)[0]
    path = os.path.join (parent_dir, directory)
    os.mkdir(path)
    for i in range(1,number_of_files+1):
        f = open(f'{directory}/file{i}.py','a')
        rand_num = randint(size/2,size)
        print(rand_num)
        for _ in range(rand_num):
            f.write(f'{chr(randint(33,126))}')

file_generator('files',3,10)