import hashlib


def part1(input):
    m = hashlib.md5(input.encode("utf-8"))
    print(m.hexdigest())


if __name__ == "__main__":
    # input = "abcdef"
    input = "abcdef609043"
    part1(input)
