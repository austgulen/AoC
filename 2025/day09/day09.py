from tqdm import tqdm


def read_file(path):
    with open(path, "r") as f:
        content = []
        for line in f:
            coord = [int(x) for x in line.replace("\n", "").split(",")]
            # content.append(line.replace("\n", ""))
            content.append(coord)
    return content


def part1(coords):
    max_a = -1
    for x, y in coords:
        # print(x, y)
        for x2, y2 in coords:
            h = abs(x - x2) + 1
            w = abs(y - y2) + 1
            a = h * w
            if a > max_a:
                # print(h, w, a)
                max_a = a
                points = [(x, y), (x2, y2)]
    print("MAX AREA = ", max_a, " for points : ", points)


def make_component(coords):
    # define the borders of the component defined by the boordinated:
    # can we find max line based on row and col, greedy?
    # for x, y in coords:
    #     None
    # xs = [c[0] for c in coords]
    # ys = [c[1] for c in coords]
    # min_x = min(coords, key=lambda c: c[0])
    # max_x = max(coords, key=lambda c: c[0])
    # min_y = min(coords, key=lambda c: c[1])
    # max_y = max(coords, key=lambda c: c[1])
    # print(min_x, max_x, min_y, max_y)
    valid_coords = []
    for x, y in tqdm(coords, desc="Filling lines"):
        if [x, y] in valid_coords:
            continue
        valid_coords.append([x, y])
        # find the straight line
        lines_x = [c[0] for c in coords if c[1] == y]
        lines_y = [c[1] for c in coords if c[0] == x]
        # print(x, y, lines_x)
        for x1 in range(min(lines_x), max(lines_x) + 1):
            if [x1, y] not in valid_coords:
                valid_coords.append([x1, y])
        for y1 in range(min(lines_y), max(lines_y) + 1):
            if [x, y1] not in valid_coords:
                valid_coords.append([x, y1])
    # fill the shape:
    for x, y in tqdm(valid_coords, desc="Filling shape"):
        lines_x = [c[0] for c in valid_coords if c[1] == y]
        lines_y = [c[1] for c in valid_coords if c[0] == x]
        # print(x, y, lines_x)
        for x1 in range(min(lines_x), max(lines_x) + 1):
            if [x1, y] not in valid_coords:
                valid_coords.append([x1, y])
        for y1 in range(min(lines_y), max(lines_y) + 1):
            if [x, y1] not in valid_coords:
                valid_coords.append([x, y1])

    print(valid_coords)
    return valid_coords


def part2(coords):
    max_a = -1
    # component = make_component(coords)
    xs = [c[0] for c in coords]
    ys = [c[1] for c in coords]
    min_x = min(coords, key=lambda c: c[0])
    max_x = max(coords, key=lambda c: c[0])
    min_y = min(coords, key=lambda c: c[1])
    max_y = max(coords, key=lambda c: c[1])
    valid_coords = make_component(coords)
    for x, y in tqdm(coords, desc="checking coords"):
        # print(x, y)
        for x2, y2 in coords:
            # check if valid:
            # if not valid(x, y, x1, y2, (min_x, max_x, min_y, max_y)):
            if not valid(x, y, x2, y2, valid_coords):
                continue
            h = abs(x - x2) + 1
            w = abs(y - y2) + 1
            a = h * w
            if a > max_a:
                # print(h, w, a)
                max_a = a
                points = [(x, y), (x2, y2)]
    print("MAX AREA = ", max_a, " for points : ", points)


def valid(x1, y1, x2, y2, valid_coords):
    p1 = [x1, y2]
    p2 = [x2, y1]
    # minx, maxx, miny, maxy = info
    print(p1, p2)
    print(valid_coords)
    valid = p1 in valid_coords and p2 in valid_coords
    print(valid)
    return p1 in valid_coords and p2 in valid_coords


def make_map(coords, part=2, example=True):
    if example:
        map = [14 * "." for _ in range(9)]
    else:
        map = ["." * 100000]  # yikes
    # for r in map:
    #     print(r)
    if part == 1:
        for x, y in coords:
            map[y] = map[y][:x] + "#" + map[y][x + 1 :]
    if part == 2:
        valid_coords = make_component(coords)
        for x, y in valid_coords:
            # vertical
            map[y] = map[y][:x] + "#" + map[y][x + 1 :]
        # also draw the line between:
        map = map  # TODO:
    return map


if __name__ == "__main__":
    # path = "example.txt"
    path = "input.txt"
    coords = read_file(path)
    map = make_map(coords)
    for r in map:
        print(r)
    # coords.sort(key=lambda sublist: sublist[1])

    part1(coords)
    part2(coords)
    # print(coords)
    # for c in coords:
    #     print(c)
