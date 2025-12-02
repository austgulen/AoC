import re
import time


def read_file(path):
    with open(path, "r") as f:
        content = f.read().replace("\n", "")
    # for l in lines:
    #     print(l)
    ranges = content.split(",")
    ranges = [r.split("-") for r in ranges]
    return ranges


def get_invalid(rang):
    # "naive" first attempt approach. Simply split the string of the number,
    # and check if the first half equals the second (in part1, invalid ids are those
    # that can be split into exactly two equal repeating parts)
    invalids = []
    # +1 to end range, since it should be included in the search.
    r = range(int(rang[0]), int(rang[1]) + 1)

    for i in r:
        str_num = str(i)
        length = len(str_num)
        if length % 2 != 0:  # if the len is odd, we can skip
            continue
        elif str_num[: length // 2] == str_num[length // 2 :]:
            invalids.append(i)
    return invalids


def get_invalid2(rang):
    invalids = []
    r = range(int(rang[0]), int(rang[1]) + 1)
    # Idea from reddit: https://www.reddit.com/r/adventofcode/comments/1pc14d1/2025_day_2_when_i_realized_the_solution_i_felt/
    # We can simply patternmatch the regexp!!
    # https://regex101.com/r/g9uPwI/1
    pattern = r"^(\d+)\1+$"
    # where:
    # ^ matches begining of string
    # (\d+) captures one or more digits (repeating can be complex)
    # \1 is "backreference", meaning \1 mathces the exact same sequence, and the + means we can have many
    # (if we remove the +, we have a match for part 1!)
    # ans $ is the end of the string
    for i in r:
        str_num = str(i)
        if re.match(pattern, str(i)):
            invalids.append(i)
    return invalids


def part1(input):
    invalids = []
    for rang in input:
        cur_invalid = get_invalid(rang)
        invalids.extend(cur_invalid)
    return sum(invalids)


def part2(input):
    invalids = []
    for rang in input:
        cur_invalid = get_invalid2(rang)
        invalids.extend(cur_invalid)
    return sum(invalids)


if __name__ == "__main__":
    path = "input.txt"
    ranges = read_file(path)
    st1 = time.perf_counter()
    part1_sol = part1(ranges)
    et1 = time.perf_counter()
    tt1 = et1 - st1

    st2 = time.perf_counter()
    part2_sol = part2(ranges)
    et2 = time.perf_counter()
    tt2 = et2 - st2
    print(f"PART 1 took {tt1:.4f} seconds: Sum of Invalid IDs: {part1_sol}")
    print(f"PART 2 took {tt2:.4f} seconds: Sum of Invalid IDs: {part2_sol}")
