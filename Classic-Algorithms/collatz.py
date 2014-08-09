#Start with a number n > 1. Find the number of steps it takes to reach one 
#using the following process: If n is even, divide it by 2. If n is odd, 
#multiply it by 3 and add 1.
import sys
import argparse
import time

def timeit(method):

    def timed(*args, **kw):
        ts = time.clock()
        result = method(*args, **kw)
        te = time.clock()

        print '%f sec' % \
              (te-ts)
        return result

    return timed

# iterative implementation
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

# recursive implementation
def collatzRecursive(n):
	if n < 1:
		return -1
	if n == 1:
		return 0
	if n % 2 == 0:
		return 1 + collatzRecursive(n/2)
	else:
		return 1 + collatzRecursive(n * 3 + 1)
	
#calculates stopping times with memoization
def stoppingTimes(n):
	store = stoppingTimes.store
	if n < 1:
		return -1
	if n == 1:
		return 0
	if n not in store:
		if n % 2:
			store[n] = 1 + stoppingTimes(n * 3 + 1)
		else:
			store[n] = 1 + stoppingTimes(n/2)
	return store[n]
stoppingTimes.store = {}

#uses the benefits of memoization
def calcAll(n):
	for i in range(n+1):
		stoppingTimes(i)
	return stoppingTimes.store[n]

def parse():
	parser = argparse.ArgumentParser(description='Calculates collatz stopping times')
	parser.add_argument("num", type=int,
			    help="number to calculate stopping time for")
	parser.add_argument("-t", "--time", action="store_true",
			    help="set this option to time the results")
	parser.add_argument("-r", "--recursive", action="store_true",
			    help="set this option to use the recursive function")
	parser.add_argument("-i", "--iterative", action="store_true",
			    help="set this option to use the iterative function")
	parser.add_argument("-m", "--memoization", action="store_true",
			    help="set this option to use memoization")
	args = parser.parse_args()
	return [args.time, args.recursive, args.iterative, args.memoization, args.num]

if __name__ == "__main__":
	args = parse()
	if not (args[0]):
		if not (args[1] or args[2] or args[3]):
			print collatzNaive(args[-1])
		if (args[1]):
			print "Recursive Result: ", collatzRecursive(args[-1])
		if (args[2]):
			print "Iterative Result: ", collatzNaive(args[-1])
		if (args[3]):
			print "Calculate All", calcAll(args[-1])
	else:
		if not (args[1] or args[2] or args[3]):
			tb = time.clock()
			tmp = collatzNaive(args[-1])
			te = time.clock()
			print "Iterative result :", tmp, " took ", (te-tb), " seconds."
		if (args[1]):
			tb = time.clock()
			tmp = collatzNaive(args[-1])
			te = time.clock()
			print "Iterative result :", tmp, " took ", (te-tb), " seconds."
		if (args[2]):
			tb = time.clock()
			tmp = collatzRecursive(args[-1])
			te = time.clock()
			print "Recursive result :", tmp, " took ", (te-tb), " seconds."
		if (args[3]):
			tb = time.clock()
			tmp = calcAll(args[-1])
			te = time.clock()
			print "Memoization result :", tmp, " took ", (te-tb), " seconds."

