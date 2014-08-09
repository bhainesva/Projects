#Start with a number n > 1. Find the number of steps it takes to reach one 
#using the following process: If n is even, divide it by 2. If n is odd, 
#multiply it by 3 and add 1.
import sys

#naive iterative implementation
def collatzNaive(n):
	if n<1:
		return -1
	if n == 1:
		return 0
	count = 0
	while (n != 1):
		#python has a weird ternary operator
		if n % 2 == 0:
			n /= 2
		else:
			n = n * 3 + 1
		count += 1
	return count

#naive recursive implementation
def collatzRecursive(n):
	if n < 1:
		return -1
	if n == 1:
		return 0
	if n % 2 == 0:
		return 1 + collatzRecursive(n/2)
	else:
		return 1 + collatzRecursive(n * 3 + 1)
	
print collatzNaive(int(sys.argv[1]))
print collatzRecursive(int(sys.argv[1]))
