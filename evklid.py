import time

def get_nod(a, b):
	"""Вычисляется НОД для двух натуральных чисел a и b
	по алгоритму Евклида."""
	while a != b:
		if a > b:
			a -= b
		else:
			b -= a
	#Какое значение возвращать не важно, так как в итоге a=b		
	return a


def test_nod(func):
	# --- тест №1 ---------
	a = 28
	b = 35
	res = func(a, b) #вызываем функцию func от двух аргументов a и b
	if res == 7:
		print("#test1 - ok")
	else:
		print("#test1 - fail")
		
	# --- тест №2 ---------
	a = 100
	b = 1
	res = func(a, b)
	if res == 1:
			print("#test2 - ok")
	else:
		print("#test2 - fail")
		
	# --- тест №3 ---------
	# для работы импортируем модуль time
	# проверка скорости работы функции
	# st начальное время, при котором запустили функцию
	# et сколько времени прошло
	# dt общее время работы
	a = 2
	b = 100000000
	st = time.time()
	res = func(a, b)
	et = time.time()
	dt = et - st
	if res == 2 and dt < 1:
			print("#test3 - ok")
	else:
		print("#test3 - fail")
		
	
		

test_nod(get_nod)		
#res = get_nod(18,24)
#print(res)
#Вызывает описание нашей функции, то что в кавычках
#help(get_nod)

