"""
	Binary Search:
	Input: a number q, called a query, a length n>1, and a sorted array X of n numbers, x_0, x_1, ..., x_n-1
		where x_i <= x_i+1 for 0 <= i <= n-1. 
	Output: the result "success" and an index b if there is a b such that q = x_b, and the result "failure" otherwise. 
"""

import random

def binary_search(q, X):
	bottom = 0
	top = len(X)
	while top - bottom > 1:
		middle_point = (bottom+top)/2
		if X[middle_point] <= q:
			bottom = middle_point
		else:
			top = middle_point
	if q == X[bottom]:
		return True
	else:
		return False

if __name__ == "__main__":
	X = [random.randrange(0, 100) for i in range(0, 30)]
	X.sort()
	q = 40
	print "X: ", X
	print "q: ", q
	result = binary_search(q, X)
	print "result: ", result

