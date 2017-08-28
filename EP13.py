"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""

import fileinput

def main():
	nums = 0
	for line in fileinput.input("EP13arr.txt"):
	    nums += int(line)
	print(nums)

if __name__ == '__main__':
	main()
