"""
Problem:

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
from math_ex import *


def main():
    vals = []
    for i in range(100, 999):
        for j in range(100, 999):
            if is_palindrome(i * j):
                vals.append(i * j)
    print(max(vals))


if __name__ == '__main__':
    main()
