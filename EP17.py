"""
If the numbers 1 to 5 are written out in words:
one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 
342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) 
contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""


def main():
    count = 0
    for i in range(1, 1001):
        count += get_ch(num_to_word(i))
    print(count)


def num_to_word(num):
    dict_word = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
                 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
                 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
                 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    dict_dec = {2: 'twen', 3: 'thir', 4: 'for', 5: 'fif',
                6: 'six', 7: 'seven', 8: 'eigh', 9: 'nine'}
    word = ''
    uni, dec, hun, tho = [num % 10, num // 10 % 10, num // 100 % 10, num // 1000]
    if tho > 0:
        word += dict_word[tho] + ' thousand'
        if num % 1000 > 0:
            word += ' and '
    if hun > 0:
        word += dict_word[hun] + ' hundred'
        if num % 100 > 0:
            word += ' and '
    if dec > 0 or uni > 0:
        if num % 100 > 19:
            if uni == 0:
                word += dict_dec[dec] + 'ty'
            else:
                word += dict_dec[dec] + 'ty-' + dict_word[uni]
        else:
            word += dict_word[dec * 10 + uni]
    return word


def get_ch(word):
    count = 0
    for ch in word:
        if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
            count += 1
    return count


if __name__ == '__main__':
    main()
