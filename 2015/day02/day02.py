def read_file(path):
    content = []
    with open(path, "r") as f:
        for line in f:
            dims = line.replace("\n", "").split("x")
            content.append([int(d) for d in dims])
    return content


def part1(dims):
    sqft_paper = 0
    for dim in dims:
        l, w, h = dim
        s1 = l * w
        s2 = w * h
        s3 = h * l
        sqft_paper += (2 * s1) + (2 * s2) + (2 * s3) + min(s1, s2, s3)
    return sqft_paper


def part2(dims):
    ft_ribbon = 0
    for dim in dims:
        l, w, h = dim
        bow = l * w * h
        ribbon = min(2 * (w + l), 2 * (h + l), 2 * (w + h))
        ft_ribbon += bow + ribbon
    return ft_ribbon


if __name__ == "__main__":
    path = "input.txt"
    # path = "example.txt"
    dims = read_file(path)
    p1 = part1(dims)
    p2 = part2(dims)
    print(p1)
    print(p2)
