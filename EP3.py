number = 600851475143
i = 2
factors = []
def is_prime(num):
	if num == 2 or num == 3:
		return True
	if num < 2 or num%2 == 0:
		return False
	for i in range(2,num/2):
		if num%i == 0:
			return False
	return True
while True:
	if is_prime(i):
		if number%i == 0:
			factors.append(i)
			number /= i
	if number == 1:
		break
	i += 1
print factors
