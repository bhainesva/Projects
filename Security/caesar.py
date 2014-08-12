# Applies a caesar cipher with key to given text
import string
import sys
import argparse

def encrypt(pt, key=13):
	return pt.translate(
			string.maketrans(
				string.ascii_uppercase + string.ascii_lowercase,
				string.ascii_uppercase[key:] + string.ascii_uppercase[:key] + 
				string.ascii_lowercase[key:] + string.ascii_lowercase[:key]
			)
	)

def decrypt(ct, key=13):
	key = 26-key
	return ct.translate(
			string.maketrans(
				string.ascii_uppercase + string.ascii_lowercase,
				string.ascii_uppercase[key:] + string.ascii_uppercase[:key] + 
				string.ascii_lowercase[key:] + string.ascii_lowercase[:key]
			)
	)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Applies caesar cipher with given text and key")
	parser.add_argument("pt", type=str,
			help="string to apply cipher to")
	parser.add_argument("key", type=int, default=13,
			help="key to use when applying cipher, defaults to ROT13")
	parser.add_argument("-d", "--decrypt", action="store_true",
			    help="set this option to decrypt")
	
	args = parser.parse_args()
	if not (args.decrypt):
		print encrypt(args.pt, args.key)
	else:
		print decrypt(args.pt, args.key)

