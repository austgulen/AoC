import numpy as np


def read_file(path):
    with open(path, "r") as f:
        content = []
        for line in f:
            coord = [int(x) for x in line.replace("\n", "").split(",")]
            # content.append(line.replace("\n", ""))
            content.append(coord)
    return content


def get_distances(coords):
    distance_matrix = []
    for coord in coords:
        # print(type(coord))
        x1, y1, z1 = coord
        # print(x1, y1, z1)
        distances = []
        for other in coords:
            # print(other)
            x2, y2, z2 = other
            # distance = round(((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5, 3)
            distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5
            distances.append(distance)
            # print(f"DIST FROM {coord} -> {other} = {distance}")
        distance_matrix.append(distances)
    distance_matrix = np.array(distance_matrix)
    return distance_matrix


def connect_curcuit(dmat, comps, return_idx=False):
    min_dist = np.min(dmat[dmat > 0])
    pos = np.where(dmat == min_dist)
    pos1, pos2 = list([int(p) for p in pos[0]])
    # new_comp = comps[pos[0]] + comps[pos[1]]
    # print(pos1, pos2)
    comps[pos1].add(pos2)
    comps[pos2].add(pos1)
    # print(comps)
    dmat = np.where(dmat == min_dist, 0, dmat)
    # update comps and dmat with transitive closure:
    closure = []
    print("NEW CONNECT FOR ", pos1, pos2)
    flag = True
    while flag:
        flag = False
        for idx in range(len(comps)):
            connections = comps[idx]
            for c in comps[idx]:
                connections = connections.union(comps[c])
                # dmat[idx, c] = 0
            if connections == comps[idx]:
                continue
            flag = True
            print(5 * " ", "UPDATED")
            comps[idx] = connections

            # transitive closure over all
            # and update the graph:
    if return_idx:
        return [pos1, pos2], dmat, comps
    return (dmat, comps)


def part1(coords, num=10):
    distance_matrix = get_distances(coords)
    # find num many connections:
    components = [set([i]) for i in range(len(distance_matrix))]
    # print(components)
    for iter in range(num):
        distance_matrix, components = connect_curcuit(distance_matrix, components)
    print()
    print(components)
    uniques = [[] * len(components)]
    for idx, c in enumerate(components):
        # uniques.append(c)
        for num in c:
            # print(num, c)
            if idx == num:
                continue
            else:
                components[num] = []
    #    print(components)
    print(components)
    lens = [len(c) for c in components]
    lens.sort(reverse=True)
    print(prod(lens[:3]))
    print(lens[:3])


def prod(lis):
    n = 1
    for i in lis:
        n *= i
    return n


def get_unique_components(components):
    components = components.copy()
    for idx, c in enumerate(components):
        for num in c:
            if idx == num:
                continue
            else:
                components[num] = []
    return components


def part2(coords):
    # do part 1 until we have a single component
    print("part2")
    distance_matrix = get_distances(coords)
    components = [set([i]) for i in range(len(distance_matrix))]
    done = False
    count = 0
    while not done:
        pos, distance_matrix, components = connect_curcuit(distance_matrix, components, return_idx=True)
        unique_components = get_unique_components(components)
        done = len(components) == len(components[0])
        # print(len(components))
        count += 1
        if count % 500 == 0:
            print(len(unique_components[0]), unique_components[0])

    p1, p2 = pos
    x1 = coords[p1][0]
    x2 = coords[p2][0]
    print(x1 * x2)


if __name__ == "__main__":
    # np.set_printoptions(linewidth=np.inf)
    # path = "example.txt"
    path = "input.txt"
    coords = read_file(path)
    distance_matrix = get_distances(coords)
    # for row in distance_matrix:
    #     print(row)
    min = np.min(distance_matrix[distance_matrix > 0])
    print("MIN = ", min, " AT : ", np.where(distance_matrix == min))
    part1(coords)
    part2(coords)
    # for row in distance_matrix:
    #     print(row)
