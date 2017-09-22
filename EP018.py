import fileinput


def main():
    nums, bits, sums = [[], [], []]
    for line in fileinput.input('EP018data.txt'):
        nums.append(list(map(int, (line[:-1].split(' ')))))
    length = len(nums[-1]) - 1
    for i in range(2**length):
        temp = 0
        summary = nums[0][temp]
        bits = get_bits(i, length)
        for (item, index) in zip(bits, range(1, len(nums[-1]))):
            temp += item
            summary += nums[index][temp]
        sums.append((summary, bits))
    print(max(sums))


def get_bits(num, size=3):
    mark = 1 << size
    bits = []
    for i in range(size):
        mark >>= 1
        bits.append((mark & num) >> (size - 1 - i))
    return bits


if __name__ == '__main__':
    main()
