def read_file(path):
    with open(path, "r") as f:
        content = []
        for line in f:
            if line.strip():
                content.append(line.replace("\n", "").strip())
    return content


def part1(diagram, row_idx, beam_col):
    # recursive sol. As it turns out from doing part2, this is not needed ...
    # there is a way easier solution, but this works atleast :') also, could
    # be usefull if we wish to visualize it later :P
    split = False
    diagram = diagram.copy()
    for idx in range(row_idx, len(diagram), 1):
        line = diagram[idx]
        # print(line)
        if line[beam_col] == "X":
            break
        if line[beam_col] == "^":
            split = True
            diagram[idx] = line[:beam_col] + "X" + line[(beam_col + 1) :]
            new_row = idx
            # print(beam_pos, idx, line, diagram[0])
            left_pos = beam_col - 1
            right_pos = beam_col + 1
            break
        if line[beam_col] != "X":
            diagram[idx] = line[:beam_col] + "|" + line[beam_col + 1 :]

    if not split:
        return 0, diagram
    left, l_diag = part1(diagram, new_row, left_pos)
    right, r_diag = part1(l_diag, new_row, right_pos)

    return (1 + left + right), r_diag


#
def strength_map(diagram, row, beam, beam_strength):
    diagram = diagram.copy()  # issues with p1/p2 is not copy
    split = False
    for idx in range(row, len(diagram), 1):
        line = diagram[idx]
        # print(line, beam)
        if line[beam] == "^":
            split = True
            # diagram[idx] = line[:beam] + str(token) + line[beam + 1 :]
            new_row = idx
            break
        if line[beam].isdigit():
            token = beam_strength + int(line[beam])
        else:
            token = beam_strength + ord(line[beam]) - 63
        if token > 9:
            token = chr(token + 63)
        diagram[idx] = line[:beam] + str(token) + line[beam + 1 :]

    if not split:
        return diagram
        # update left and right beam with new strength
    # print(beam_strength)
    left_map = strength_map(diagram, new_row, beam - 1, beam_strength)
    right_map = strength_map(left_map, new_row, beam + 1, beam_strength)
    return right_map


def part2_old(diagram):
    # idea: update the map with the "beam strength". Then, we can count it after?
    # Does not work on final input. 2 reasons, 1. the chr can (and does) turn into ^. even
    # with this mitigated, we still have issues with the size of the largest numbers. Instead,
    # We do as discussed on the reddit. This is essencially the same idea, but smarter. Instead
    # of actually writing the beams onto the diagram, we just keep a list of beam col idxs.
    # This does what we tried to do here
    beam_pos = diagram[0].index("S")
    # define strength of beam:
    diagram = [row.replace(".", "0") for row in diagram]
    for l in diagram:
        print(l)
    map = strength_map(diagram, 1, beam_pos, 1)
    for s in map:
        print(s)
    total = 0
    for beam in map[-1]:
        if beam.isdigit():
            total += int(beam)
        else:
            total += ord(beam) - 63
    print(total)


#


def part2(diagram):
    # Issue with storing beam info as token! try to keep a running sum in w for loop?
    # Turns out, we do not need any recursion. Original solution was to "draw" the beam w/ strength
    # directly on the map. This works on the sample solution, but the numbers get large, so chr(num) does
    # not work. After giving up on trying to effectively tokenize the recusive approach, the reddit
    # discussion provided a Way smarter idea. that is to just keep a running total list per col idx...
    # where this approach was suggested. This seems to be a way more elegant idea that I first attempted. Thx to
    # user Koosman from r/Adventofcode for the insight!
    beams = [0] * len(diagram[0])
    beams[diagram[0].index("S")] = 1
    for row in diagram:
        # this is the next row, so make a temp.
        # This ensures that beams stop, and that the count is correct!
        temp = [0] * len(row)
        for idx, chr in enumerate(row):
            if chr == "^":
                # split if there is a beam hitting it:
                temp[idx - 1] += beams[idx]
                temp[idx + 1] += beams[idx]
            else:
                # otherwise, the beam keeps going down (like the visual from p1 we added)
                temp[idx] += beams[idx]
        beams = temp
    return beams


def part2_recursive(diagram, beam_pos, beams):
    # memoization
    # local = [0] * len(diagram[0])
    # beams[diagram[0].index("S")] = 1\
    # print(row_idx)
    split = False
    diagram = diagram.copy()
    for idx in range(len(diagram)):
        # print(beams)
        # print(idx, row_idx, len(diagram))
        line = diagram[idx]

        # print(line, beam_pos)
        if line[beam_pos] == "^":
            split = True
            # new_row = idx
            diagram = diagram[idx:]
            # print(beam_pos, idx, line, diagram[0])
            left_pos = beam_pos - 1
            right_pos = beam_pos + 1
            beams[left_pos] += 1
            beams[right_pos] += 1
            # beams[beam_pos] = #max(0, beams[idx] - 1)
            break
    # print(beams)
    if not split:
        # print(beams)
        return beams
    left_beams = part2_recursive(diagram, left_pos, beams)
    # print(left_beams)
    right_beams = part2_recursive(diagram, right_pos, left_beams)
    # print(left_beams, right_beams)
    return right_beams  # [right_beams[i] + left_beams[i] for i in range(len(right_beams))]


if __name__ == "__main__":
    path = "example.txt"
    # path = "input.txt"
    diagram = read_file(path)
    beam_col = diagram[0].index("S")
    p1, diag = part1(diagram, 0, beam_col)
    for line in diag:
        print(line)

    # print(nonrecursive_part1(diagram))
    beams = part2(diagram)
    p2 = sum(beams)
    print("NUMBER OF BEAM SPLITS : ", p1)
    print("NUMBER OF TIMELINES   : ", p2)
    part2_old(diagram)
    beams = [0] * len(diagram[0])
    beam_pos = diagram[0].index("S")
    beams[beam_pos] = 1
    a = part2_recursive(diagram, beam_pos, beams)
    print(a, sum(a))
    # s = 0
    # for r in diag:
    #     for c in r:
    #         if c == "X":
    #             s += 1
    # print(s)
    # for l in diag:
    #     print(l)


# def nonrecursive_part1(diagram):
#     beams = [False] * len(diagram[0])
#     beams[diagram[0].index("S")] = True
#     # print(beams)
#     splits = 0
#     for row in diagram:
#         # print(beams)
#         temp = [False] * len(row)
#         for idx, chr in enumerate(row):
#             # print(chr)
#             if chr == "^" and beams[idx]:
#                 # print(row, beams[idx])
#                 temp[idx - 1] = True
#                 temp[idx + 1] = True
#                 # print(temp)
#                 # split if applicable
#                 # if beams[idx] > 0:
#                 splits += 1
#                 # print(temp)
#                 # print(temp)
#                 # print(temp, splits)
#             else:
#                 temp[idx] = beams[idx] or temp[idx]
#         beams = temp
#
#     return splits

# def upadte_and_remove(diagram, pos):
#     # update and remve splitter when hit
#     split = False
#     for idx, line in enumerate(diagram):
#         if line[beam_pos] == "^":
#             split = True
#             diagram[idx] = line[:pos] + "X" + line[pos + 1 :]
#             break
#         diagram[idx] = line[:pos] + "|" + line[pos + 1 :]
#     if not split:
#         return 0, diagram
# def strength_map(diagram, row, beam, beam_strength):
#     diagram = diagram.copy()  # issues with p1/p2 is not copy
#     split = False
#     for idx in range(row, len(diagram), 1):
#         line = diagram[idx]
#         # print(line, beam)
#         if line[beam] == chr(9):
#             split = True
#             # diagram[idx] = line[:beam] + str(token) + line[beam + 1 :]
#             new_row = idx
#             break
#         # if line[beam].isdigit():
#         #     token = beam_strength + int(line[beam])
#         # else:
#         # token = beam_strength + ord(line[beam]) - 55
#         # if token > 9:
#         token = 1 + ord(line[beam]) + 9
#         print(token)
#         token = chr(token)
#         if token == "^":
#             print("ERROR!! TOKEN IS ^")
#         diagram[idx] = line[:beam] + str(token) + line[beam + 1 :]
#
#     if not split:
#         return diagram
#         # update left and right beam with new strength
#     # print(beam_strength)
#     left_map = strength_map(diagram, new_row, beam - 1, beam_strength)
#     right_map = strength_map(left_map, new_row, beam + 1, beam_strength)
#     return right_map


# def apply_beam(diagram, row_idx, beam_col):
#     diagram = diagram.copy()
#     for idx in range(row_idx, len(diagram), 1):
#         line = diagram[idx]
#         # print(line)
#         if line[beam_col] == "^":
#             split = True
#             diagram[idx] = line[:beam_col] + "X" + line[(beam_col + 1) :]
#             new_row = idx
#             # print(beam_pos, idx, line, diagram[0])
#             left_pos = beam_col - 1
#             right_pos = beam_col + 1
#             break
#         if line[beam_col] != "X":
#             diagram[idx] = line[:beam_col] + "|" + line[beam_col + 1 :]
#
#     if not split:
#         return 0, diagram
#     left, l_diag = part1(diagram, new_row, left_pos)
#     right, r_diag = part1(l_diag, new_row, right_pos)
