"""
	Shortest Path:
	Input: a distance matrix D with entries d_ij for 1 <= i, j <= n where d_ij is the length of the direct path from i to j. 
	Output: a matrix D where entry d_ij is the length of the shortest path from i to j. 
"""

import numpy as np

def shortest_path(D):
	m, n = D.shape
	for k in range(n):
		for i in range(n):
			for j in range(n):
				D[i][j] = min(D[i][j], D[i][k]+D[k][j])
	return D

def symmetric_mat_generator(n):
	D = np.random.randint(100, size=(n, n))
	return (D + D.T)/2

if __name__ == "__main__":
	n = 20
	D = symmetric_mat_generator(n)
	D_short = shortest_path(D)
	print "D: \n", D
	print "D_short: \n", D_short
