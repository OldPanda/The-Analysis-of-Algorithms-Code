"""
	Triangular Matrix Addition:
	Input: a size n and two triangular matrices A and B with elements a_ij and b_ij for 1 <= j <= i <= n. 
	Output: matrix C = A + B
"""

import numpy as np

def triangular_matrix_addition(n, A, B):
	C = np.zeros((n, n))
	for i in range(n):
		for j in range(i+1):
			C[i][j] = A[i][j] + B[i][j]
	return C

if __name__ == "__main__":
# A test case
	n = 10
	A = np.random.randint(100, size = (n, n))
	A_tril = np.tril(A)
	B = np.random.randint(100, size = (n, n))
	B_tril = np.tril(B)
	C = triangular_matrix_addition(n, A_tril, B_tril)
	print "A: \n"
	print A_tril
	print "B: \n"
	print B_tril
	print "C: \n"
	print C
