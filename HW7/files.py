#Задание 1: Дан файл с произвольным текстом, необходимо найти все числа в файле и записать в список numbers

f = open('text.txt', 'r')
data = f.readline()
data_list = ''
while data:
    for i in data:
        if not i.isdigit():
            data = data.replace(i, ' ')
    data_list += data
    data = f.readline()

numbers = [i for i in data_list.split(' ') if i.isdigit()]
print(numbers)

#Задание 2: Запросить у пользователя текст и записать его в файл data.txt

