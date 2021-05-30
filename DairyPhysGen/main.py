import sqlite3
import datetime
from random import randint, choice, seed, shuffle
from resource import *

con = sqlite3.connect('database.db')
cur = con.cursor()
file = open('Output.txt','w')
dates = []

print('Выберите уровень сложности из списка: Легкий Нормальный Средний Тяжелый Терминатор')
level = input()
print('Введите начальную дату в формате: Год-Месяц-День')
y,m,d = map(int, input().split('-'))
paste = datetime.datetime(y, m, d)

now = datetime.datetime.today()
y1,m1,d1 = map(int, str(now).split(' ')[0].split('-'))
if (d1+1>days_in_month[m1]) or (d1+2>days_in_month[m1]):
    m1 += 1
    d1 = 1
else:
    d1 += 1
d1 += 2
now = datetime.datetime(y1,m1,d1)

while paste.isoweekday() not in [2,5]:
    if d+1>days_in_month[m]:
        m += 1
        d = 1
    else:
        d += 1
    paste = datetime.datetime(y, m, d)

while now.isoweekday() not in [2,5]:

    if d1-1<0:
        m1 -= 1
        d1 = days_in_month[m1]
    else:
        d1 -= 1
    now = datetime.datetime(y1, m1, d1)

while (now-paste).days>1:
    if d+1>days_in_month[m]:
        m += 1
        d = 1
    else:
        d += 1
    paste = datetime.datetime(y,m,d)
    if paste.isoweekday() in [2,5]:
        dates.append(str(paste).split(' ')[0])

cur.execute(f'SELECT start FROM start_table WHERE ID = 1')
start = cur.fetchall()[0][0]

cur.execute(f'SELECT action FROM actions WHERE level = "{level}"')
actions = cur.fetchall()

cur.execute(f'SELECT end FROM end_table')
end = cur.fetchall()

for i in dates:
    y,m,d = map(int, i.split('-'))
    file.write(f'{d} {Dmonth[m]} {y}г\n')

for i in range(len(dates)//2):
    seed()
    result = f'\nПродолжительность занятия {randint(30,40)} мин\n \nРазминка:\n'
    result += start
    result += "\nОсновная часть:\n  2 круга из 3 упражнений\n"
    
    for j in range(3):
        shuffle(actions)
        shuffle(Light)
        result += f'{j+1}. {choice(actions)[0]} {choice(Light)} раз\n'
    
    result += f"\nОтдых между кругами {randint(2,5)} мин\n"
    result += "\nЗаключение:\n"
    
    for j in range(3):
        shuffle(end)
        shuffle(Light)
        result += f'{j+1}. {choice(end)[0]} {choice(Light)} раз\n'
    
    file.write(f'{sep}\nПульс: До {randint(63,69)} После {randint(150,165)}\nСамочувствие {choice(Health)}\nЖелание {choice(Motivation)}\n\n')
    file.write(result)
    shuffle(Health)
    shuffle(Motivation)

print('Готово')