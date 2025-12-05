def read_file(path):
    with open(path, "r") as f:
        content = []
        for line in f:
            content.append(line.strip())
        # content = f.readlines()
    return content


def part1(grid):
    rolls = 0
    for ridx in range(len(grid)):
        for cidx in range(len(grid[ridx])):
            if grid[ridx][cidx] == "@":
                rolls += int(check_valid(grid, ridx, cidx))
    return rolls


def part2(grid):
    rolls = 0
    flag = True
    print("\nSTARTING GRID")
    for row in grid:
        print(row)
    while flag:
        flag = False
        new_map = grid.copy()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "@":
                    if check_valid(grid, row, col):
                        flag = True
                        # print(grid[row], type(grid[row]))
                        # print("ROW ", row, "INDEX ", col)
                        # print("BEFORE : ", new_map[row])
                        new_map[row] = new_map[row][:col] + "X" + new_map[row][col + 1 :]
                        # print("AFTER: ", new_map[row])
                        rolls += 1
        grid = new_map
    print("\nFINAL GRID")
    for row in grid:
        print(row)
    return rolls


def check_valid(grid, row, col):
    # there can at most be 3 rolls around the idx
    # Messy, but whatever. it runs :^)
    count = 0
    for r in range(row - 1, row + 2, 1):
        if r < 0 or r >= len(grid):
            continue
        for c in range(col - 1, col + 2, 1):
            if c < 0 or c >= len(grid[row]):
                continue
            if r == row and c == col:
                continue
            if grid[r][c] == "@":
                count += 1
    return count < 4


if __name__ == "__main__":
    # path = "example.txt"
    # path = "input.txt"
    grid = read_file(path)
    print(part1(grid))
    print(part2(grid))
