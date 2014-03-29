"""
	Linear Search:
	Input: an array X of numbers with elements x_i for 1 <= i <= n, and a query q. 
	Output: a number i such that q = x_i if there is such an i or i = n + 1 otherwise. 
"""

import random

def linear_search(q, X):
	for i in range(len(X)):
		if q == X[i]:
			return i
	return len(X)

if __name__ == "__main__":
# A simple test case
	n = 30
	X = [random.randint(0, 100) for i in range(n)]
	q = 50
	i = linear_search(q, X)
	print "X: ", X
	print "q: ", q
	print "X["+str(i)+ "]: "+str(X[i])+" and q: "+str(q) if i < n else "Not found q"
