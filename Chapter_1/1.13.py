"""
	Binary Merge:
	Input: fila A with elements a_1 through a_m and file B with b_1 through b_n. Each file is sorted in increasing order. The first element in each file is element 1. When elements are output from a file, you should think of the remaining elements as being renumbered so that once again the first remaining element is element 1. 
	Output: file C in sorted order with all the elements from A and B. 
	For simplicity, I only use list to denote A, B, and C. 
"""

import random
import math

# This function is modified from 1.6.py
def binary_search(q, X, length):
	bottom = 0
	top = length
	middle_point = (bottom + top)/2
	while top - bottom > 0:
		middle_point = (bottom + top)/2
		if q < X[middle_point]:
			top = middle_point
		elif q > X[middle_point]:
			if bottom == middle_point:
				return middle_point
			bottom = middle_point
		else:
			return middle_point
	return middle_point

def binary_merge(A, B):
	m = len(A)
	n = len(B)
	C = []
	while m > 0 and n > 0:
		if m > n:
			t = int(math.floor(math.log(float(m)/n, 2)))
			if B[0] >= A[2 ** t - 1]:
				m -= 2 ** t
				for index in range(2 ** t):
					C.append(A.pop(0))
				continue
			else:
				i = binary_search(B[0], A, 2 ** t)
				for index in range(i):
					C.append(A.pop(0))
				C.append(B.pop(0))
				n -= 1
				m -= i
				continue
		else: 
			t = int(math.floor(math.log(float(n)/m, 2)))
			if A[0] >= B[2 ** t - 1]:
				n -= 2 ** t
				for index in range(2 ** t):
					C.append(B.pop(0))
				continue
			else:
				i = binary_search(A[0], B, 2 ** t)
				for index in range(i):
					C.append(B.pop(0))
				C.append(A.pop(0))
				m -= 1
				n -= i
				continue
	if m > 0:
		C.extend(A)
	elif n > 0:
		C.extend(B)
	return C

if __name__ == "__main__":
	m = 30
	n = 40
	A = [random.randint(0, 100) for i in range(m)]
	A.sort()
	B = [random.randint(0, 100) for i in range(n)]
	B.sort()
	print "A: ", A
	print "B: ", B
	C = binary_merge(A, B)
	print "C: ", C
