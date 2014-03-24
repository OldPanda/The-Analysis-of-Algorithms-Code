"""
	Integer Value:
	Input: an integer which is represented by its base, b, its length minus one, n, 
		and its digits d_n, d_n-1, ..., d_1, d_0, where n>=0. 
	Output: v, the value of the integer. 
	It is assumed that the value of the integer will fit in one computer word. 
"""

def integer_value(b, n, d_list):
	i = n
	v = 0
	while True:
		v = v*b+d_list[i]
		i -= 1
		if i < 0:
			break
	return v

if __name__ == "__main__":
# Select some integers to test it. 
	b = 10
	n = 4
	d_list = [1, 2, 3, 4, 5]
	result = integer_value(b, n, d_list)
	print "The result is ", result, " when the base is ", b, ", the length is ", n+1, ", and the d_list is ", d_list
