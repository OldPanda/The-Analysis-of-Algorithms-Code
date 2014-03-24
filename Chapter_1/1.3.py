"""
	This is the for-loop version of algorithm 1.2. Input and output remain the same. 
"""

def integer_value(b, n, d_list):
	v = 0
	for i in range(n, -1, -1):
		v = v*b + d_list[i]
	return v

if __name__ == "__main__":
# A test case
	b = 10
	n = 4
	d_list = [1, 2, 3, 4, 5]
	result = integer_value(b, n, d_list)
	print "The result is ", result, " when the base is ", b, ", the length is ", n+1, ", and the d_list is ", d_list
