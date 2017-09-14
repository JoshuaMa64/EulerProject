"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
"""
def sum_of_digits(num):
	digits = []
	for i in str(num):
		digits.append(int(i))
	return sum(digits)

def main():
	print(sum_of_digits(2**1000))

if __name__ == '__main__':
	main()
