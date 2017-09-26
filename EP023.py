"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though
it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""


def main():
    ab = [i for i in range(1, 28123) if is_abundant(i)]
    sum_of_ab = list(set([x + y for x in ab for y in ab if x + y <= 28123]))
    sum_of_not_ab = sum([i for i in range(1, 28123) if i not in sum_of_ab])
    print(sum_of_not_ab)


def is_abundant(num):
    divs = [1]
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            divs.append(i)
    return sum(divs) > num


if __name__ == '__main__':
    main()
