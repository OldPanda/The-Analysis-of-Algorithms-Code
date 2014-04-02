"""
	Random Hashing:
	Data structure: a key array X with entries x_i for 0 <= i <= N-1 and a corresponding record array R. 
	Initial conditions: the number of entries, k, is zero and each key location, x_i, contains the value empty, a special value that is not the value of any key. 
	Input: a query, q. 
	Output: a location i such that q = x_i if there is such an i (i.e., q is in the table) or i such that x_i contains empty and the hash algorithm would look in location x_i when looking for q. 
"""

import numpy as np

X = np.random.randint(10, size=10)
R = np.random.randint(100, size=10)

# A simple function
def f(h, q):
	return (h*2 + q)%10

def random_hashing(q):
	h = 0
	while True:
		h = h + 1
		i = f(h, q)
		if X[i] == 0:
			return False
		elif X[i] == q:
			return True

if __name__ == "__main__":
	print X
	print "Query 5: ", random_hashing(5)
	print "Query 6: ", random_hashing(6)
