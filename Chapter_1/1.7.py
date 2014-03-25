# /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python
"""
	Matrix Addition:
	Input: two n*m matrices A, B with elements a[i][j] and b[i][j] for 1 <= i <= n, 1 <= j <= m. 
	Output: the n*m matrix C with elements c[i][j] for 1 <= i <= n, 1 <= j <= m where C = A + B
"""

import numpy as np

def matrix_addition(A, B):
	n, m = A.shape
	C = np.zeros(shape = A.shape)
	for i in range(n):
		for j in range(m):
			C[i][j] = A[i][j] + B[i][j]
	return C

if __name__ == "__main__":
	n = 6
	m = 6
	A = np.random.randint(100, size = (n, m))
	B = np.random.randint(100, size = (n, m))
	print "A: ", A
	print "B: ", B
	C = matrix_addition(A, B)
	print "C: ", C
