#Занятия проходят по понедельникам и четвергам в 19:15
# Первое занятие произошло 17.10.2022. Всего 32 занятия.
# Вывести список всех занятий в таком формате (номера лекций выровнены по правому краю):
#
# Lecture  1: 17 Oct 2022 19:15
# Lecture  2: 20 Oct 2022 19:15
# ...
# Lecture  9: 14 Nov 2022 19:15
# Lecture 10: 17 Nov 2022 19:15
# ...
# Lecture 32: 02 Feb 2023 19:15

from datetime import timedelta, datetime,date

start = datetime(2022, 10, 17, 19, 15)
start_str = start.strftime('%d %b %Y  %H:%M')
delta1 = timedelta(days=3)
delta2 = timedelta(days=4)

lst =[]

for i in range(32):
    start_str = start.strftime ('%d %b %Y  %H:%M')
    if i % 2 == 0:
        lst.append(f'Lecture {i+1}: {start_str}')
        start += delta1
    else:
        lst.append(f'Lecture {i+1}: {start_str}')
        start += delta2

for i, el in enumerate(lst):
    if i < 9:
        el = el.split (' ')
        el[1] = ' ' + el[1]
        el = ' '.join(el)
    print(el)
