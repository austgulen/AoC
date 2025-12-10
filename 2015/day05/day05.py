def read_file(path):
    content = []
    with open(path, "r") as f:
        for line in f:
            content.append(line.replace("\n", ""))
    return content


def part1(strings):
    banned = ["ab", "cd", "pq", "xy"]
    vowels = "aeiou"
    doubles = [2 * c for c in "abcdefghijklmnopqrstuvwxyz"]
    # print(doubles)
    total_nice = 0
    for s in strings:
        naughty = any([b in s for b in banned])

        num_vowels = len([c for c in s if c in vowels]) >= 3
        contains_doubles = any([d in s for d in doubles])
        # print(s, naughty, num_vowels, contains_doubles)

        total_nice += int(num_vowels and contains_doubles and not naughty)

    return total_nice

def part2(strings):
# lets do regexp again! :D e


if __name__ == "__main__":
    path = "input.txt"
    # path = "example.txt"
    strings = read_file(path)
    print(len(strings))
    p1 = part1(strings)
    print(p1)
    # for s in strings:
    #     print(s)
