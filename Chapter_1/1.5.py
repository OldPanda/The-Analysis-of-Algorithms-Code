"""
	Euclidean:
	Input: positive integers m and n. 
	Output: integers d, a, and b such that d is the greatest common divisor of m and n, and such that am+bn=d. 
"""

def euclidean(m, n):
	a_prime = b = 0
	a = b_prime = 1
	d = m
	r = n
	q = 0
	while r > 0:
		c = d
		d = r
		t = a_prime-q*a
		a_prime = a
		a = t
		t = b_prime-q*b
		b_prime = b
		b = t
		# Divede
		q = c/d
		r = c%d # Thus q is the quotient and r is the remainder of c divided by d
	return d, a, b

if __name__ == "__main__":
# Test case
	m = 100
	n = 70
	d, a, b = euclidean(m, n)
	print "The gcd of ", m, " and ", n, " is ", d, ". And a = ", a, ", b = ", b
	m = 439
	n = 345
	d, a, b = euclidean(m, n)
	print "The gcd of ", m, " and ", n, " is ", d, ". And a = ", a, ", b = ", b

