import sys
import time

def reverseRecursive(istr):
	if len(istr) <= 1:
		return istr
	return reverseRecursive(istr[1:]) + istr[0]

def reverseSlice(istr):
	return istr[::-1]

if __name__ == "__main__":
	print "Recursive: " + reverseRecursive(sys.argv[1])		
	print "Slice: " + reverseSlice(sys.argv[1])		
