def read_file(path):
    with open(path, "r") as f:
        content = []
        for line in f:
            # line.replace(P)
            content.append(line.replace("\n", ""))
        # content = f.readlines()
    return content


def transpose(sheet):
    return list(zip(*sheet))


def prod(ls):
    p = 1
    for n in ls:
        p *= n
    return p


def part1(sheet):
    # transpose to get each eq on the same line:
    total = 0
    sheet = [l.strip().split() for l in sheet]
    flipped_sheet = transpose(sheet)
    for eq in flipped_sheet:
        nums = [int(n) for n in eq[:-1]]
        # print(eq, nums)
        # print(eq)
        if eq[-1] == "+":
            total += sum(nums)
        else:
            total += prod(nums)
    return total


def part2(sheet):
    # split into list of chars:
    total = 0
    # for s in sheet:
    #     print(s)
    sheet = [list(r) for r in sheet]
    # for s in sheet:
    #     print(s)
    lines = transpose(sheet)
    # create the calcs
    equations = []
    cur_eq = []
    for l in lines:
        print(l)
        if l[-1] == "+" or l[-1] == "*":
            # new operator, means new equations
            # equations.append(cur_eq)
            cur_eq = [l[-1]]
            num = int("".join(l[:-1]))
            cur_eq.append(num)
            continue
        line = "".join(l).split()
        # print(line)
        if not line:
            # print("Empty", line)
            equations.append(cur_eq)
        else:
            cur_eq.append(int(line[0]))
        # print("".join(eq))
    equations.append(cur_eq)  # the last one aswell!
    # print((equations))
    for eq in equations:
        if eq[0] == "+":
            res = sum(eq[1:])
        else:
            res = prod(eq[1:])
        total += res
        # print(eq, res, 10 * " ", total)

    return total


if __name__ == "__main__":
    path = "example.txt"
    path = "input.txt"
    sheet = read_file(path)
    print(part1(sheet))
    print(part2(sheet))
