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
import json
#
import xml.etree.ElementTree as ET

tree = ET.parse('pages.xml')

root = tree.getroot()

json_dict = {}

for element in root:
    key = list(element.attrib.keys())[0]
    json_dict[element.attrib[key]] = {}
    keys = {}
    keys2 = {}
    for el1 in element:
        key1 = list (el1.attrib.keys())[0]
        keys.update({el1.attrib[key1]: {}})
        json_dict[element.attrib[key]] = keys
        for el2 in el1:
            key2 = list (el2.attrib.keys ())[0]
            key3 = list (el2.attrib.keys ())[1]
            keys2.update ({el2.attrib[key2] : []})
            json_dict[element.attrib[key]][el1.attrib[key1]][el2.attrib[key2]] = [el2.attrib[key3],el2.text]



out_file = open ("json_data.json", "w")

json.dump (json_dict, out_file, indent=4)

out_file.close()



