"""
	Horner's Method: 
	Input: The value of a variable x and a polynomial
		p(x) = a_n*x^n + a_n-1*x^n-1 + ... + a_1*x + a_0
		given by its degree n>=0 and its coefficent a_0, ..., a_n.
	Output: The value, v, of the polynomial evaluated at x. 
"""

def horner_method(x, a_list):
	i = len(a_list) - 1
	v = 0
	while True:
		v = v*x + a_list[i]
		i -= 1
		if i < 0:
			break
	return v

if __name__ == '__main__':
# Arbitrarilly select a_lists and x's to test the code. 
	a_list = [1, 2, 1]
	x = 3
	result = horner_method(x, a_list)
	print "The result is ", result, " when a_list is ", a_list, " and x is ", x
	
	a_list = [1, 3, 3, 1]
	x = 4
	result = horner_method(x, a_list)
	print "The result is ", result, " when a_list is ", a_list, " and x is ", x
