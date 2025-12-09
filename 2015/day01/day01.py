def read_file(path):
    with open(path) as f:
        content = f.read().replace("\n", "")
    return content


def part_1(input):
    count = 0
    for chr in input:
        if chr == ")":
            count -= 1
        else:
            count += 1
    return count


def part2(input):
    floor = 0
    for pos, chr in enumerate(list(input)):
        if chr == ")":
            floor -= 1
        else:
            floor += 1
        if floor < 0:
            return pos + 1


if __name__ == "__main__":
    path = "example.txt"
    # path = "input.txt"
    input = read_file(path)
    p1 = part_1(input)
    p2 = part2(input)
    print("THE FINAL FLOOR OF SANTA               :", p1)
    print("BASEMENT ENTERED FOR THE FIRST TIME AT :", p2)
