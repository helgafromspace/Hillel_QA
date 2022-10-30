# Задание 1:Пользователь вводит слово, если это слово является полиндромом, то вывести '+', иначе '-'

# word = input('Enter your word: ').lower()
# if word == word[::-1] and word.isalpha() and len(word) > 1:
#     print('+')
# else:
#     print('-')

# Задание 2: Пользователь вводит текст и слово которое нужно найти, если это слово есть в тексте, вывести 'YES', иначе 'NO'

# text = input('Enter your text: ')
# substring = input('Enter word you\'re looking for: ')
#
# if substring in text:
#     print('YES')
# else:
#     print('NO')

# Задание 3:Пользователь вводит строку. Если она начинается на 'abc', то заменить их на 'www', иначе добавить в конец строки 'zzz'

# user_input = input('Enter your string: ')
#
# if user_input.startswith('abc'):
#     user_input = user_input.replace('abc', 'www')
# else:
#     user_input += 'zzz'
# print(user_input)

# Задание 4: Пользователь вводит текст, удалить в тексте все цифры и вывести строку пользователю.

# 1
# text = input('Enter your text: ')
# for i in text:
#     if i.isdigit():
#         text = text.replace(i, '')
# print(text)

# 2
# text = input('Enter your text: ')
# text_alpha = ''
# for i in text:
#     if i.isalpha():
#         text_alpha += i
# print(text_alpha)

# Задание 5: Написать валидатор для почты. Пользователь вводит почту, а программа должна проверить, что в почте есть символ '@' и '.',
# и если это так, то вывести "YES", иначе "NO"



#1
# if '@' in email and '.' in email:
#     print('YES')
# else:
#     print('NO')

#2 Учла не все условия, но для примера: один символ @ в строке, наличие @ в строке, точка в доменной части урлы, хотя бы один символ в именной части урлы,
# хотя бы один символ между @ и точкой, хотя бы 2 символа в области урлы где домен верхнего уровня(после последней точки), чтобы спецсиволы и пробел не использовались в качестве символа

# flag = False
# sym_flag = False
# while not flag:
#     email = input('Enter your email: ')
#     if email != '':
#         flag = True
#         if email.count('@') == 1 and '@' in email and '.' in email[email.index('@') + 1:] and len(email[:email.index('@')]) > 0 and len(email[email.index('@') + 1:email.rfind('.')]) > 0 and len(email[email.rfind('.') + 1:]) > 1:
#             for i in email:
#                 if i in ['<', '>', '(', ')', '[', ']', ',', ';', ':', '\\', '/', '"', ' ']:
#                     print('NO')
#                     sym_flag = True
#                     break
#             if not sym_flag:
#                 print('YES')
#         else:
#             print('NO')
#     else:
#         print('Email can\'t be empty field')
