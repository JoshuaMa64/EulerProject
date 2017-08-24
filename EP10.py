from math import *
from time import clock

def is_prime(num):
	if num == 2 or num == 3:
		return True
	if num<2 or num%2 == 0:
		return False
	for i in range(3,int(sqrt(num)+1)):
		if num%i == 0:
			return False
	return True
t = clock()
sum = 0
for i in range(2000000):
	if i%100000 == 0:
		print i
	if is_prime(i):
		sum += i
print sum
print clock() - t
