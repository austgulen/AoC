def read_file(path):
    with open(path, "r") as f:
        content = []
        for line in f:
            content.append(line.replace("\n", ""))
    return content


# Helpers
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
    # not very efficient i think, but the most intuitive way
    # (at least to me)
    total = 0
    # split into list of chars: [12 3] -> ['1','2','','3']
    sheet = [list(r) for r in sheet]
    lines = transpose(sheet)
    # create the eqsto be calculated
    equations = []
    cur_eq = []
    for l in lines:
        if l[-1] == "+" or l[-1] == "*":
            # new operator, means new equations
            cur_eq = [l[-1]]  # add the operator first
            num = int("".join(l[:-1]))
            cur_eq.append(num)
            continue
        line = "".join(l).split()
        if not line:
            # line is empty, we have the full eq,
            # append it to eqs
            equations.append(cur_eq)
        else:
            # otherwise, we are not done
            cur_eq.append(int(line[0]))
    equations.append(cur_eq)  # the last one aswell!
    # loop over again. innefficient, but easier to read imo
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
