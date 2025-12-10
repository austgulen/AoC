import ast

import matplotlib.pyplot as plt
import networkx as nx


class DecitionTree:
    def __init__(self, size, button_wiring):
        self.root = [0] * size
        self.button_wiring = button_wiring
        self.tree = self.build_tree()

    # def build_tree(self):
    #     # simmulate the whole tree:
    #
    #
    # def traverse(self, start_pos, action)


def read_file(path):
    content = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip().split(" ")
            # split the input
            light_diagram = get_light(line[0])
            button_wiring = get_wiring(line[1:-1])
            joltage = get_joltage(line[-1])
            # print(light_diagram, button_wiring, joltage)
            content.append([light_diagram, button_wiring, joltage])
    return content


def get_wiring(connections):
    new_connections = []
    for c in connections:
        args = c[1:-1].split(",")
        connection = tuple([int(x) for x in args])
        new_connections.append(connection)
    return new_connections


def get_light(diagram):
    # drop bracks
    new_diag = []
    diagram = diagram[1:-1]
    for c in diagram:
        new_diag.append(c == "#")
    return tuple(new_diag)


def get_joltage(requirements):
    # strip brackets
    reqs = [int(x) for x in requirements[1:-1].split(",")]
    return reqs


def push_button(state, button):
    # print(state, button)
    new_state = list(state)
    for idx in button:
        new_state[idx] = not state[idx]

    return tuple(new_state)


def build_digraph(root, buttons):
    G = nx.DiGraph()
    G.add_node(root)
    cur_state = root
    added = [root]
    while added:
        cur_state = added.pop()
        # print("STATE = ", cur_state)
        for b in buttons:
            change = False
            # print(buttons, b)
            new_state = push_button(cur_state, b)
            if new_state == root:  # or new_state in G:
                continue
            if new_state not in G:
                added.append(new_state)
            # print(f"{cur_state} -> {b} -> {new_state}")
            G.add_node(new_state)
            G.add_edge(cur_state, new_state)
        # added = new_added

    return G


def part1(manual):
    total = 0
    for machine in manual:
        # print(machine)
        lights = machine[0]
        buttons = machine[1]
        initial_config = tuple([False] * len(lights))
        # print(lights, initial_config)
        dg = build_digraph(initial_config, buttons)
        # print(nx.shortest_path(dg, initial_config, tuple(lights)))
        min_pushes = len(nx.shortest_path(dg, source=initial_config, target=tuple(lights))) - 1
        # print(f"min pushes to reach {lights} from {initial_config} = {min_pushes}")
        total += min_pushes
    return total


def part2(manual):
    None


if __name__ == "__main__":
    # path = "example.txt"
    path = "input.txt"
    manual = read_file(path)
    p1 = part1(manual)
    print("SUM OF MINIMUM PRESSES : ", p1)
