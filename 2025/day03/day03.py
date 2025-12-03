def read_file(path):
    with open(path, "r") as f:
        content = []
        for line in f:
            content.append(line.strip())
        # content = f.readlines()
    return content


def part1(betteries):
    joltage = 0
    for b in batteries:
        joltage += find_max(b, 2)

    return joltage


def part2(batteries):
    joltage = 0
    for b in batteries:
        num = recursive_max(b, 11)
        print(b, num)
        joltage += num
    return joltage


def find_max(battery, digits):
    # naive first:
    # find left:
    ptr = 0
    left = -1
    for idx in range(len(battery) - 1):
        if int(battery[idx]) > left:
            left = int(battery[idx])
            ptr = idx
        if left == 9:
            break
    # while ptr < len(battery) - 1 and int(battery[ptr]) < 9:
    #     if int(battery[ptr]) > left:
    #         left = int(battery[ptr])
    #     ptr += 1
    left *= 10
    right = -1
    for bank in battery[ptr + 1 :]:
        if int(bank) > right:
            right = int(bank)
    print(battery, left, right, left + right)
    return left + right


def recursive_max(battery, n):
    # we always want the biggest digit at each step.
    # I think we can just greedy pick the max. If there
    # are 2 or more of the max, pick the first occuring?
    if n == -1:
        return 0
    ptr = 0
    num = -1
    for idx in range(len(battery) - n):
        print(battery, idx, n)
        if int(battery[idx]) > num:
            num = int(battery[idx])
            ptr = idx
        if num == 9:
            break
    return (10**n * num) + recursive_max(battery[ptr + 1 :], n - 1)


if __name__ == "__main__":
    path = "input.txt"
    # path = "example.txt"
    batteries = read_file(path)
    print(part1(batteries))
    print(part2(batteries))
