"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""
from math import factorial


def main():
    print(combination(20, 40))


def combination(m, n):
    if m != 0:
        result = factorial(n) / (factorial(m) * factorial(n - m))
    else:
        result = 1
    return result

if __name__ == '__main__':
    main()
