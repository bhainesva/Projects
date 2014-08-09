import re
import sys

#doing it this way is probably slower because it searches 5 times
#but I think it's clean
def countVowels(istr):
	vowels = ["a", "e", "i", "o", "u"]
	results = {}
	for vowel in vowels:
		results[vowel] = len(re.findall(vowel, istr, re.IGNORECASE))
	return results

if __name__ == "__main__":
	counts = countVowels(sys.argv[1])
	total = 0
	for key in counts:
		total += counts[key]
		print key + ": ", counts[key]
	print "Total: ", total
