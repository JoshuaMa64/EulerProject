import math


def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num < 2:
        return False
    for i in range(3, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


def is_palindrome(word):
    str1 = ''
    length = len(str(word))
    word = str(word)
    for i in range(1, length + 1):
        str1 += word[-i]
    if str1 == word:
        return True
    else:
        return False
