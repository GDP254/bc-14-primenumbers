from math import sqrt

def prime_nums(n):
	if type(n) != int:
		raise TypeError()
	if n < 0:
		raise ValueError()
	rslt = []
	for x in range(0, n):
		if is_prime(x):
			rslt.append(x)
	return rslt

""" 
Based on.
Title: Prime Numbers
Author: James Conan
Date: N/A
Code version: Pseudocode
Availability: http://www.cs.uwc.ac.za/~jconnan/FirstYear/checkprime.txt 
"""
def is_prime(num):
	if num < 2:
		return False # not prime
	pfactor = 2
	srt = sqrt(num)
	while (pfactor <= srt) and not (num % pfactor == 0):
		pfactor += 1
	if pfactor <= srt:
		return False # not prime
	else:
		return True # prime

"""
Asymptotic analysis
	- The iteration within the prime_nums function with run n + 1 times. 
	- The extra iteration detects the conditions necessary for exiting the loop.
	- On each iteration, the function is_prime is called with the current value of x as an arguement.
	- This arguement is used to determine the number of iterations within the the is_prime function.
	- The code represents a nested loop which has a complexity of O(n^2) i.e. quadratic complexity.
	- It is however unlikely that this worst scenario will occur since the nested loop is capped to the square root of the input.
"""