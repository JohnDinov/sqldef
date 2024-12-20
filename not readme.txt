
$  Данные я получил, вот как их впихать в #creat.execute("INSERT INTO users VALUES ('Pavlik', 'Coca', 100005, 2, 'Наркоша')") 

$  Я думал что можно через F строку creat.execute("INSERT INTO users VALUES f({name}, {surname}, {userid}, {balance}, {role})")

$  Щас попробую

Майкл
Джордан
100006
4900
Спортсмен

#   Traceback (most recent call last):
#     File "Ь:\Users\python\Desktop\sq\main.py", line 35, in <module>
#       creat.execute("INSERT INTO users VALUES f({name}, {surname}, {userid}, {balance}, {role})")
#   sqlite3.OperationalError: near "f": syntax error

$  !Облом!

$  а нет я тупой, F строка же перед ковычками


#    Traceback (most recent call last):
#    File "Ь:\Users\python\Desktop\sq\main.py", line 28, in <module>
#        creat.execute("INSERT INTO users VALUES f'({name}, {surname}, {userid}, {balance}, {role})'")
#    sqlite3.OperationalError: near "f": syntax error

$  мда..

#   Traceback (most recent call last):
#   File "Ь:\Users\python\Desktop\sq\main.py", line 27, in <module>
#       creat.execute("INSERT INTO users VALUES f'{name}, {surname}, {userid}, {balance}, {role}'")
#   sqlite3.OperationalError: near "f": syntax error

$ Кайф.............


$ Я иду правильно но у меня скорее проеб с методом добавления данных через переменные.




creat.execute("INSERT INTO users VALUES (@name)")
creat.execute("INSERT INTO users VALUES (@surname)")
creat.execute("INSERT INTO users VALUES (@userid)")
creat.execute("INSERT INTO users VALUES (@balance)")
creat.execute("INSERT INTO users VALUES (@role)")

$  проеб. . . я устал



$ Так это тоже не работает......

creat.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)", (None, name, surname, userid, balance, role))

#   Traceback (most recent call last):
#     File "Ь:\Users\python\Desktop\sq\main.py", line 21, in <module>
#       creat.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)", (None, name, surname, userid, balance, role))
#   sqlite3.ProgrammingError: Incorrect number of bindings supplied. The current statement uses 5, and there are 6 supplied.
#   PS Ь:\Users\python\Desktop\sq>




$  Ебать я идиот.............

Джордан
Майкл
100006
4900
Спортсмен

1 Fanny Minecrafter 100001 200 Человек
2 Bob Frankalina 100002 300 Ангелок
3 Ron Lonso 100003 250 Шайтан
4 Lola Minsitar 100004 1250 Гоблин
5 Pavlik Coca 100005 2 Наркоша
6 Джордан Майкл 100006 4900 Спортсмен
PS Ь:\Users\python\Desktop\sq> py .\main.py


Илья
Даунский
100007
720
Строитель

1 Fanny Minecrafter 100001 200 Человек
2 Bob Frankalina 100002 300 Ангелок
3 Ron Lonso 100003 250 Шайтан
4 Lola Minsitar 100004 1250 Гоблин
5 Pavlik Coca 100005 2 Наркоша
6 Джордан Майкл 100006 4900 Спортсмен
7 Илья Даунский 100007 720 Строитель
PS Ь:\Users\python\Desktop\sq>




$  работает...................

$  Ошибка в том, что я запрашиваю 6 значений а передаю 5 
$  creat.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)", (None, name, surname, userid, balance, role))
$  none здесь не нужноооо
$  юхууууууууууууууу
$  работает
$  Босс, надеюсь ты горд за меня))


$  Теперь функцию, я без понятия зачем она здесь и как её делать

Итог код на данный момент



import sqlite3

db = sqlite3.connect('user.db')

# Создание курсора
creat = db.cursor()

#creat.execute("""CREATE TABLE users (
#   name text,
#   surname text,
#   id integer,
#   balance integer,
#   role text
#)""")

# Я предпологаю что нужно создать переменные сначала,
name, surname = input(), input()
userid, balance = int(input()), int(input())
role = input()

creat.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)", (name, surname, userid, balance, role))
#creat.execute("DELETE FROM users WHERE rowid = 4")

#creat.execute("UPDATE users SET role = 'Шайтан' WHERE rowid = 3")

creat.execute("SELECT rowid, * FROM users WHERE id > 1")
items = creat.fetchall()
#print(creat.fetchall())
#print(creat.fetchmany())
#print(creat.fetchone()[5])
    
for el in items:
    print(el[0],'-' el[1],'-' el[2],'-' el[3],'-' el[4],'-' el[5])

db.commit()
db.close()
