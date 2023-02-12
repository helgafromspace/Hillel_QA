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
    page_name_key = list(element.attrib.keys())[0]
    json_dict[element.attrib[page_name_key]] = {}
    keys_el_name = {}
    keys_locators = {}
    for el1 in element:
        el_name = list (el1.attrib.keys())[0]
        keys_el_name.update({el1.attrib[el_name]: {}})
        json_dict[element.attrib[page_name_key ]] = keys_el_name
        for el2 in el1:
            platform = list (el2.attrib.keys ())[0]
            locator_type = list (el2.attrib.keys ())[1]
            keys_locators.update ({el2.attrib[platform] : []})
            json_dict[element.attrib[page_name_key]][el1.attrib[el_name]][el2.attrib[platform]] = [el2.attrib[locator_type],el2.text]



out_file = open ("json_data.json", "w")

json.dump (json_dict, out_file, indent=4)

out_file.close()



