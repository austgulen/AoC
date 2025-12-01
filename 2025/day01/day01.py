# get the quick py solution:


def read_file(path):
    with open(path, "r") as f:
        lines = f.readlines()
    # for l in lines:
    #     print(l)
    return lines


def solve_part1(input):
    # It is a dial from 0-99, i.e. %100
    cur_pos = 50  # dial always starts at 50
    sol = 0
    for instruction in input:
        if cur_pos == 0:
            sol += 1
        if instruction[0] == "L":  # left -> -
            cur_pos -= int(instruction[1:])
        else:
            cur_pos += int(instruction[1:])
        cur_pos = cur_pos % 100
    return sol


def solve_part2(input):
    # It is a dial from 0-99, i.e. %100
    # need to check stops at 0 AND passes.
    dial = 50  # dial always starts at 50
    # https://www.reddit.com/r/adventofcode/comments/1pb85u9/comment/nrootdk/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

    sol = 0
    for instruction in input:
        dir = instruction[0]
        ticks = int(instruction[1:])

        if dir == "L":  # left -> -
            # Need an extra check here, if we are at 0,
            # we do not count it as crossing.
            cur_num = dial - ticks
            passes = abs(cur_num // 100)
            # avoid overcounting
            if dial == 0:
                passes -= 1
            if passes > 0:
                print("LEFT ROTATION")
                print(dial, ticks, cur_num, passes)
            dial = cur_num % 100
            # check if we end up on 0
            if dial == 0:
                passes += 1

        elif dir == "R":  # right
            # check not needed here, as it is implicitly included in the floor div
            cur_num = dial + ticks
            passes = cur_num // 100
            dial = cur_num % 100

        # if dial == 0:
        #     sol += 1

        sol += passes

        # # Bruteforce counting the clicks:
        # while cur_pos != (cur_pos % 100):
        #     if cur_pos < 0:
        #         cur_pos += 100
        #     else:
        #         cur_pos -= 100
        #     sol += 1
    return sol


# bruteforce to check for "correct value"
def bruteforce(input):
    None


if __name__ == "__main__":
    file_path = "input.txt"
    # file_path = "test.txt"
    input = read_file(file_path)
    ans1 = solve_part1(input)
    ans2 = solve_part2(input)
    print("Number of times we hit 0: ", ans1)
    print("Number of times we pass/hit 0:", ans2)
