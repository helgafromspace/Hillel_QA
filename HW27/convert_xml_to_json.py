"""
Написать скрипт, который преобразовывает xml файл в json файл.

Файлы находятся здесь:

https://github.com/AlexLitvino/hl_pyauto_17oct22/tree/master/L25/HW

Исходный xml файл содержит узлы страниц и элементов, атрибутами указаны имена страниц, элементов и типы локаторов элементов.
Текст элемента указывает значение локатора.

json файл должен хранить словарь-страниц, страница должна быть словарем элементов, ключи словаря элемента соответствуют платформе,
а значения - список из типа локатора и значения локатора.

Мутно описано, смотрите примеры файлов:)

"""
#
import xml.etree.ElementTree as ET

tree = ET.parse('pages.xml')
#
# # print(tree)
#
root = tree.getroot()
# # print(len(root))

json_dict = {}

for element in root:
    key = list(element.attrib.keys())[0]
    # print(element.attrib[key])
    # keys.append(element.attrib[key])
    json_dict[element.attrib[key]] = {}
    keys = {}
    keys2 = {}
    for el1 in element:
        key1 = list (el1.attrib.keys())[0]
        # print(element.attrib[key])
        # print(el1.attrib)
        keys.update({el1.attrib[key1]: {}})
        # print(el1.attrib[key1])
        json_dict[element.attrib[key]] = keys
        for el2 in el1:
            key2 = list (el2.attrib.keys ())[0]
            key3 = list (el2.attrib.keys ())[1]
            # print(el2.attrib)
            print(key2)
            print(el2.attrib[key3])
            keys2.update ({el2.attrib[key2] : []})
            json_dict[element.attrib[key]][el1.attrib[key1]][el2.attrib[key2]] = [el2.attrib[key3],el2.text]

# print(keys)
# print(keys1)
print(json_dict)

# print(json_dict)



