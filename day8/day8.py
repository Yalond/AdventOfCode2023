import re
import itertools
from math import lcm

dirs, _, *rows = open("input1.txt", "r").readlines()
directions = ["LR".index(d) for d in dirs.strip()]
nodes_map = {node: (l, r) for node, l, r in (re.findall(r"\w{3}", row) for row in rows)}

def find_goal(start_item, is_goal):

    prev_item = start_item
    for i, direction in enumerate(itertools.cycle(directions)):
        prev_item = nodes_map[prev_item][direction]
        if is_goal(prev_item): return i + 1
    return 0
    
print(f'p1: {find_goal("AAA", lambda x: x == "ZZZ")}')
print(f'p2: {lcm(*(find_goal(start, lambda g: g[2] == "Z") for start in nodes_map if start[2] == "A"))}')