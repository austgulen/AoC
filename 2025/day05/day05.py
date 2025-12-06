def read_file(path):
    # read and split
    rules, data = [], []
    ptr = 0
    with open(path, "r") as f:
        for line in f:
            l = line.strip()
            if not l:
                ptr += 1
                continue
            if ptr == 0:
                low, high = l.split("-")
                # print(low, high)
                rules.append([int(low), int(high)])
            else:
                data.append(int(l))
    return rules, data


def part1(rules, data):
    ranges = unify_ranges(rules)
    count = 0
    for d in data:
        # print(d)
        for r in ranges:
            if d in range(r[0], r[1] + 1):  # + 1, since it is inclusive
                count += 1
                # print(4 * " ", "yes")
                break
            # print("no")
    return count


def unify_ranges(rules):
    # the idea is to avoid checking all ranges, since many overlap
    # we then sort and combine them
    rules.sort()
    ranges = [rules[0]]
    for r in rules:
        start, end = r
        # print(start, end)
        if start > ranges[-1][1]:
            ranges.append([start, end])
        else:
            # print(end)
            ranges[-1][1] = max(end, ranges[-1][1])
    return ranges


def part2(rules):
    # since we already implemented the unify ranges function,
    # part 2 becomes easy!
    ranges = unify_ranges(rules)
    sum = 0
    for r in ranges:
        sum += r[1] - r[0] + 1  #! +1 since the range is inclusive
    return sum


if __name__ == "__main__":
    path = "example.txt"
    # path = "input.txt"
    rules, data = read_file(path)
    # print(rules)
    rules.sort()
    # for r in rules:
    #     print(r)
    # for d in data:
    #     print(d)
    print("Number of fresh ingredients available: ", part1(rules, data))
    print("Number of fresh     IDs     available: ", part2(rules))
