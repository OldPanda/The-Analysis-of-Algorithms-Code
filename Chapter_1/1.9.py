"""
	Matrix Multiplication: 
	Input: an n*p matrix A with elements a_ij and a p*m matrix B with elements b_ij. 
	Output: the n*m matrix C with elements c_ij, where C = A*B. 
"""

import numpy as np

def matrix_multiplication(A, B):
	n, p = A.shape
	p, m = B.shape
	C = np.zeros(shape = (n, m))
	for i in range(n):
		for j in range(m):
			C[i][j] = 0
			for k in range(p):
				C[i][j] = C[i][j] + A[i][k] * B[k][j]
	return C

if __name__ == "__main__":
	n = 10
	p = 3
	m = 7
	A = np.random.randint(100, size = (n, p))
	B = np.random.randint(100, size = (p, m))
	print "A: ", A
	print "B: ", B
	C = matrix_multiplication(A, B)
	print "C: ", C
