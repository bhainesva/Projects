# Applies a caesar cipher with key to given text
import string
import sys
import argparse

def caesar(pt, key=13):
	return pt.translate(
			string.maketrans(
				string.ascii_uppercase + string.ascii_lowercase,
				string.ascii_uppercase[key:] + string.ascii_uppercase[:key] + 
				string.ascii_lowercase[key:] + string.ascii_uppercase[:key]
			)
	)
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Applies caesar cipher with given text and key")
	parser.add_argument("pt", type=str,
			help="string to apply cipher to")
	parser.add_argument("key", type=int, default=13,
			help="key to use when applying cipher, defaults to ROT13")
	args = parser.parse_args()
	print caesar(args.pt, args.key)

