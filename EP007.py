count = 0
number = 2


def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(2, num / 2):
        if num % i == 0:
            return False
    return True


while True:
    if is_prime(number):
        count += 1
        print(count)
    if count == 2333:
        break
    number += 1
print(number)
