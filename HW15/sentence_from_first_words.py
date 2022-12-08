#Есть фрагмент текста, состоящий из предложений.

# Предложение - это строка, которая начинается с большой буквы и заканчивается точкой, вопросительным или восклицательным знаком (или несколькими такими знаками).
# Слова состоят только из латинских букв, разделяются отделяются пробелами или запятыми с пробелами.
# Предложение может состоять из одного слова.
# Составить предложение из первых слов предложений фрагмента.
# Только первое слово итогового предложения должно быть с большой буквы, остальные с маленькой.
# Предложение должно заканчиваться точкой.
#
# def generate_sentence(text: str) -> str:
#
#   pass

# "Hello, cocroach. And where it is? Who, can do it?! Or vice versa!? Yes, it's difficult... Claro.." -> "Hello and who or yes claro."
#
# "Hola..." -> Hola.

import re

text = "Hello, Alex cocroach. And where it is? Who, can do it?! Or vice versa!? Yes, it's difficult... Claro.."
# text = "Hola..."
# pattern = '[A-Z]\w*'
# re_obj = re.compile(pattern)
# res = re_obj.findall(text)
# res2 = ''
# for i, word in enumerate(res):
#     if i == 0:
#         res2 += word + ' '
#     else:
#         res2 += word.lower() + ' '
# res2 = res2.strip() + '.'
#
# print(res2)


pattern = '[A-Z]'
re_obj = re.compile(pattern)
res = re_obj.findall(text)

print(res)
