from math import sqrt

def prime_nums(n):
	if type(n) != int:
		raise TypeError()
	if n < 0:
		raise ValueError()
	rslt = []
	for x in range(0, n):
		if isPrime(x):
			rslt.append(x)
	return rslt

def isPrime(num):
	if num < 2:
		return False # not prime
	pfactor = 2
	while (pfactor <= sqrt(num)) and not (num % pfactor == 0):
		pfactor += 1
	if pfactor <= sqrt(num):
		return False # not prime
	else:
		return True # prime

"""


"""