#Computes pi to the input number of decimal places using BBP
#en.wikipedia.org/wiki/Bailey-Borwein-Plouffe_formula
#result is in hex
#Might try updating to use bellard/base10
from __future__ import division
import sys
import math

def S(j, digit):
	left = 0
	right = 0
	for k in range(digit+1):
		left += (16**(digit-k) % (8*k + j)) / (8*k + j)
		lef = left % 1.0
	k = digit + 1
	#http://en.literateprograms.org/Pi_with_the_BBP_formula_%28Python%29
	#for how to approximate sums to infinity
	#previously I just picked a random upper bound
	while 1:
		nRight = right + (16**(digit-k)) / (8*k + j)
		if nRight == right:
			break;
		else:
			right = nRight
		k += 1
	return left + right

def getPi_n(n):
	x = (4*S(1, n) - 2*S(4, n) - S(5, n) - S(6, n)) % 1
	return format(int(x * 16), 'x')

if __name__ == "__main__":
	n = sys.argv[1]
	if int(n) > 100:
		print "Use a number <= 100"
	else:
		result = []
		for i in range(int(n)):
			result.append(getPi_n(i))
		print "3." + ''.join(result)

