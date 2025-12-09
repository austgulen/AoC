def read_file(path):
    with open(path) as f:
        content = f.read().replace("\n", "")
    return content


def part1(flightpath, return_visited=False):
    # houses = 1
    cur_pos = (0, 0)
    visited = set([cur_pos])
    for dir in flightpath:
        match dir:
            case "^":
                # go up:
                cur_pos = (cur_pos[0], cur_pos[1] + 1)
            case "v":
                # go down
                cur_pos = (cur_pos[0], cur_pos[1] - 1)
            case ">":
                # go right
                cur_pos = (cur_pos[0] + 1, cur_pos[1])
            case "<":
                # go left
                cur_pos = (cur_pos[0] - 1, cur_pos[1])
        visited.add(cur_pos)
    if return_visited:
        return visited
    return len(visited)


def part2(flighpath):
    santa_list = flighpath[0::2]
    robo_list = flighpath[1::2]
    santa_visited = part1(santa_list, return_visited=True)
    robo_visited = part1(robo_list, return_visited=True)
    combined = santa_visited.union(robo_visited)
    print(len(combined))


if __name__ == "__main__":
    path = "input.txt"
    # path = "example.txt"
    input = read_file(path)
    # print(input)
    p1 = part1(input)
    print(p1)
    part2(input)
