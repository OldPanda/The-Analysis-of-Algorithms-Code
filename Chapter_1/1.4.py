"""
	Addition:
	Input: a base b, a length n, and two positive n digit integers X and Y. 
	Intermediate variable: c, the carry. 
	Output: an integer Z represented by its digits such that Z = X + Y, or an error if X + Y cannot
		be represented as an n digit, base b integer. 
"""

import math
import random

# This function comes from 1.3.py
def integer_value(b, n, d_list):
	v = 0
	for i in range(n-1, -1, -1):
		v = v*b + d_list[i]
	return v

def addition(b, n, X, Y):
	c = 0
	Z = []
	for i in range(0, n):
		s = X[i] + Y[i] + c
		Z.append(s%b)
		c = math.floor(s/b)
	if c != 0:
		Z.append(c)
		i += 1
	i += 1
	return Z, i

if __name__ == "__main__":
# A test case
	b = 10
	n = 30
	X = [random.randrange(0, 10) for i in range(0, n)]
	Y = [random.randrange(0, 10) for i in range(0, n)]
	print "X: ", integer_value(b, n, X)
	print "Y: ", integer_value(b, n, Y)
	Z, Z_length = addition(b, n, X, Y)
	print "Z: ", integer_value(b, Z_length, Z)

