# Evklid-algoritm

Алгоритм Евклида(медленный)

Найдем НОД(наибольший общий делитель) для двух натуральных чисел a и b.

Так же выполним тестирование написанной функции.

Пусть есть два числа a=18 и b=24, чтобы найти НОД надо из большего вычесть меньшее.

b-a=24-18=6 это значение запишем в переменную которая хранит большее значение,
то есть в b. b=b-a

На следующей итерации у нас a=18, b=6.
a=a-b=18-6=12

Следующая итерация
a=a-b=12-6=6

a=6, b=6 значения одинаковы, это и есть результат работы данного алгоритма.

Можно записать, пока a!=b
находим большее среди a и b, уменьшаем большее на величину меньшего. 
Выводим полученное значение величины a или b.


Алгоритм Евклида(быстрый)

a = 2
b = 100
b = b - a = 100- 2 = 98
b = 98 - 2 = 96
b = 96 - 2 = 94
...
b = 4 - 2 = 2
b = 2 - 2 = 0

или это все можно записать как b = b % a = 0 
То есть серия этих вычитаний, это вычисление остатка от деления.

Например a = 18 b = 24
b = 24 % 18 = 6
a = 18 % 6 = 0
НОД(18, 24) = 6

Пока меньшее число больше 0, большему числу присваиваем остаток от деления на меньшее число, выводим большее число.
