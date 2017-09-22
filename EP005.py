"""
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
"""
from math_ex import is_prime

num = 1
for i in [x for x in range(20) if is_prime(x)]:
    num *= i
num = num * (2**3) * 3
print(num)
