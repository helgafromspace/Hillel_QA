# 1. Написать функцию, которая возвращает слуайную строку заданной длины.
# Строка должна состоять из больших и маленьких латинских букв и цифр.

# def get_random_string(length: int) -> str:
#   pass
#
# Ограничения:
# - Не использовать модуль string
# - Не создавать руками список ['a', 'b', 'c', ..., 'X', 'Y', 'Z', 0, 1, ..., 8, 9]

from random import *

def get_random_string(length: int) -> str:
    random_string = ''
    for i in range(length):
        char = chr(randint(48, 122))
        if char.isalnum():
            random_string += char
        else:
            random_string += chr(randint(48, 57))
    return random_string

print(get_random_string(8))