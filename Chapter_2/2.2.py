"""
	Quicksort:
	Input: bound l and r, and an array X with elements x_l-1, ..., x_r+1 where l <= r anf for l <= i <= r, x_l-1 <= x_i <= x_r+1. 
	Output: a sorted permutation of the array X so that for l-1 <= i <= r, x_i <= x_i+1. 
"""

import random

"""
	Split:
	Input: an array X, a lower limit l, and an upper limit r, with l <= r. The array X is partly sorted so that, for l <= j <= r, x_l-1 <= x_j <= x_r+1. 
	Output: a splitting index i such that l <= i <= r, and a permutation of the elements x_l, ..., x_r such that for l <= j <= i, x_j <= x_i, and for i <= j <= r, x_i <= x_j. 
"""
def split(X, l, r):
	i = l
	j = r
	x = X[i]
	while True:
		while l <= j and j <= r and X[j] > x:
			j -= 1
		if j <= i:
			X[i] = x
			return X, i
		X[i] = X[j]
		i += 1
		while l <= i and i <= r and X[i] < x:
			i += 1
		if j <= i:
			X[j] = x
			i = j
			return X, i
		X[j] = X[i]
		j -= 1

def quicksort(X, l, r):
	if l >= r:
		return X
	else:
		X, i = split(X, l, r)
		X = quicksort(X, l, i-1)
		X = quicksort(X, i+1, r)
		return X

if __name__ == "__main__":
	n = 30
	X = [random.randint(0, 100) for i in range(n)]
	print "X: ", X
	X_sort = quicksort(X, 0, n-1)
	print "X_sort: ", X_sort

