import fileinput


def main():
    nums = []
    summary = 0
    for line in fileinput.input('EP18data.txt'):
        nums.append(list(map(int, (line[:-1].split(' ')))))
    for j in range(2**(len(nums[-1]) - 1)):
        print(j, end=' ')
    print(summary)

def get_bits(num, size=3):
    mark = 1 << size
    bits = []
    for i in range(size):
        mark >>= 1
        bits.append((mark & num) >> (size - 1 - i))
    return bits

if __name__ == '__main__':
    main()
