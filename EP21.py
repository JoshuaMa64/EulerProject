"""
Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b,
then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284.

The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


def main():
    amicable_nums = []
    for i in range(10000):
        temp = d(i)
        if i == d(temp) and i != temp and (temp, i) not in amicable_nums:
            amicable_nums.append(i)
            # amicable_nums.append(i, temp)
    print(sum(amicable_nums))


def d(num):
    divs = [1]
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            divs.append(i)
    return sum(divs)


if __name__ == '__main__':
    main()
