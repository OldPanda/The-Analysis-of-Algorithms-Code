"""
	Multiplication:
	Input: a base b, a length n, and two n-digit integers X and Y. 
	Output: a 2n-digit integer Z represented by its digit such that Z = XY. 
"""

import random

def integer_value(b, n, d_list):
	v = 0
	for i in range(n-1, -1, -1):
		v = v*b + d_list[i]
	return v

def multiplication(b, n, X, Y):
	Z = [0 for i in range(2*n)]
	for i in range(n):
		carry = 0
		for j in range(n):
			p = X[i]*Y[j] + Z[i+j] + carry
			Z[i+j] = p%b
			carry = p/b
		Z[i+n]=carry
	return Z

if __name__ == "__main__":
	b = 10
	n = 30
	X = [random.randrange(b) for i in range(n)]
	Y = [random.randrange(b) for i in range(n)]
	print "X: ", integer_value(b, n, X)
	print "Y: ", integer_value(b, n, Y)
	Z = multiplication(b, n, X, Y)
	print "Z: ", integer_value(b, 2*n, Z)

