"""
	Heapsort:
	Input: an array X with elements x_i for 1 <= i <= N. 
	Output: an array X that is a sorted rearrangement of the input. 
"""

import random

"""
	Heap:
	Input: a starting place l, an ending place r, and an array X, where X ebeys the "almost heap" property for the subtree starting at position l. 
	Output: an array X rearranged so that the heap condition, x_i >= x_2i and x_i >= x_2i+1, is satisfied for l = i and for any elements that are rearranged. 
"""
def heap(l, r, X):
	x = X[l]
	j = l
	while True:
		i = j
		j = 2 * j
		if j > r:
			break
		if j < r and X[j] < X[j + 1]:
			j += 1
		if x < X[j]:
			X[i] = X[j]
		else:
			break
	X[i] = x
	return X

def heapsort(X):
	N = len(X) - 1
	for l in range(N/2, -1, -1):
		X = heap(l, N, X)
		print "Build heap: ", X
	for r in range(N - 1, 0, -1):
		X[0], X[r + 1] = X[r + 1], X[0]
		X = heap(0, r, X)
		print "Rebuild: ", X
	X[1], X[0] = X[0], X[1]
	return X

if __name__ == "__main__":
	X = [random.randint(0, 100) for i in range(10)]
	print "X: ", X
	X_sorted = heapsort(X)
	print "X_sorted: ", X_sorted
