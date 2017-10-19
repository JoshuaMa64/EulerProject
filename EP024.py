"""
A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
from math import factorial as fac


def main():
    numbers = list('0123456789')
    rank = 1000000
    rank -= 1
    permutation_need = ''
    for i in range(10)[::-1]:
        index = rank // fac(i)
        rank = rank - fac(i) * index
        permutation_need += numbers[index]
        numbers.remove(numbers[index])
    print(permutation_need)


if __name__ == '__main__':
    main()
