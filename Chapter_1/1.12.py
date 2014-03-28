"""
	Insertion Sort:
	Input: a size n, n >= 2, and an array of numbers X with elements x_i for 1 <= i <= n. 
	Output: a sorted permutation of X such that x_i <= x_j for 1 <= i < j <= n. 
"""

import random

# This algorithm is modified to avoid the use of goto. 
def insertion_sort(n, X):
	for j in range(1, n):
		temp = X[j]
		i = j-1
		while i >= 0 and X[i] >= temp:
			X[i+1] = X[i]
			i -= 1
		X[i+1] = temp
	return X

if __name__ == "__main__":
	n = 40
	X = [random.randint(0, 1000) for i in range(n)]
	print "X: ", X
	X_sorted = insertion_sort(n, X)
	print "X_sorted: ", X_sorted
