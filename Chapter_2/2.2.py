"""
	Quicksort:
	Input: bound l and r, and an array X with elements x_l-1, ..., x_r+1 where l <= r anf for l <= i <= r, x_l-1 <= x_i <= x_r+1. 
	Output: a sorted permutation of the array X so that for l-1 <= i <= r, x_i <= x_i+1. 
"""

X = []

def split(X, i, l, r):
	pass

def quicksort(X, l, r):
	if l >= r:
		return
	else:
		split(X, i, l, r)
		quicksort(X, l, i-1)
		quicksort(X, i+1, r)
		return

