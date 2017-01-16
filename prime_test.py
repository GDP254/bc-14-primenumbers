from unittest import TestCase
from prime import prime_nums

"""
	Requirements: A working function to generate prime numbers from 0 to n with asymtotic analysis
	1. n should be an integer
	2. when n is 40 output should be [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
	3. n should not be negative
"""

class TestPrime(TestCase):
	def test_string_input(self):
		with self.assertRaises(TypeError):
			prime_nums("String")

	def test_list_input(self):
		with self.assertRaises(TypeError):
			prime_nums(["list"])

	def test_dictionary_input(self):
		with self.assertRaises(TypeError):
			prime_nums({"String"})

	def test_float_input(self):
		with self.assertRaises(TypeError):
			prime_nums(4.0)

	def test_tuple_input(self):
		with self.assertRaises(TypeError):
			prime_nums(("tuple"))

	def test_null_input(self):
		with self.assertRaises(TypeError):
			prime_nums(None)

	def test_boolean_input(self):
		with self.assertRaises(TypeError):
			prime_nums(True)

	def test_complex_input(self):
		with self.assertRaises(TypeError):
			prime_nums(1j)

	def test_negative_input(self):
		with self.assertRaises(ValueError):
			prime_nums(-8)

	def test_prime(self):
		self.assertEquals(prime_nums(40), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])

if __name__ == '__main__':
	unittest.main()