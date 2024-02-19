from collections import deque

join_map = {
    (1, 0): ["|", "L", "J"],
    (-1, 0): ["|", "F", "7"],
    (0, -1): ["-", "L", "F"],
    (0, 1): ["-", "J", "7"],
}
# row, col not x, y
input_map = {
    "|": [(1, 0), (-1, 0)],
    "-": [(0, -1), (0, 1)],
    "F": [(1, 0), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(0, -1), (-1, 0)],
    "7": [(1, 0), (0, -1)]
    }

box_shape = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]

box_positions = {
    "|": [[(1, 0)], [(-1, 0)]],
    "-": [[(0, -1)], [(0, 1)]],
    "F": [[(1, 1)], [(0, -1), (-1, -1), (-1, 0)]],
    "L": [[(-1, 1)], [(0, -1), (1, 0), (1, -1)]],
    "J": [[(-1, -1)], [(0, 1), (1, 0), (1,1)]],
    "7": [[(1, -1)], [(0, 1), (-1, 1), (-1, 0)]]
}

start_dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def add_pos(a, b): return (a[0] + b[0], a[1] + b[1])

def in_range(pos, size):
    return pos[0] >= 0 and pos[1] >= 0 and pos[0] < size[0] and pos[1] < size[1]

def can_add(point, offset, grid):
    return in_range(point, (len(grid), len(grid[0]))) and (grid[point[0]][point[1]] in join_map[offset])

def proc(filename):

    start_point = None

    adj = {}
    grid = []

    for row in open(filename, "r").readlines():
        grid_row = []
        for elem in row.strip():
            grid_row.append(elem)
        grid.append(grid_row)

    for i, row in enumerate(grid):
        for j, symbol in enumerate(row):

            pos = (i, j)

            if symbol == "S": 
                start_point = pos
                adj[start_point] = []
                for direction in start_dirs:
                    offset_pos = add_pos(start_point, direction)
                    if can_add(offset_pos, direction, grid): 
                        adj[start_point].append(offset_pos)
                        if offset_pos not in adj: adj[offset_pos] = []
                        adj[offset_pos].append(start_point)


            if not pos in adj: adj[pos] = []

            if symbol in input_map:

                s1 = input_map[symbol][0]
                s2 = input_map[symbol][1]

                a = add_pos(pos, s1)
                b = add_pos(pos, s2)
                
                if can_add(a, s1, grid): adj[pos].append(a)
                if can_add(b, s2, grid): adj[pos].append(b)
                
    return start_point, adj, grid 

def find_max_cycle_dist(start_point, adj):

    seen_items = set([start_point])
    open_set = [start_point]
    simple_path = [] 

    while len(open_set) > 0:

        current_item = open_set.pop()
        simple_path.append(current_item)
        seen_items.add(current_item)

        if current_item in adj:
            for neighbour in adj[current_item]:
                if neighbour not in seen_items:
                    open_set.append(neighbour)

    return simple_path[:-1]

def regen_grid(input_grid, boundry_path):

    output_grid = []
    boundry_path_set = set(boundry_path)

    output_grid = []
    for i, row in enumerate(input_grid):
        output_grid_row = []
        for j, symbol in enumerate(row):
            if (i, j) in boundry_path_set:
                output_grid_row.append(symbol)
            else:
                output_grid_row.append(".")
        output_grid.append(output_grid_row)

    count = 0;
    for i, row in enumerate(output_grid):
        inside = False
        wall_start = None
        for j, symbol in enumerate(row[:-1]):

            if symbol == "|": inside = not inside

            if symbol in ["F", "L"]:
                wall_start = symbol
            
            if wall_start == "F" and symbol in ["J"]:
                inside = not inside
                wall_start = None

            if wall_start == "L" and symbol in ["7"]:
                inside = not inside
                wall_start = None

            if output_grid[i][j] == "." and inside: count += 1

    return count

def proc_file(filename):

    start, adj, grid = proc(filename)
    path = find_max_cycle_dist(start, adj)
    count = regen_grid(grid, path)

    print(filename)
    print("p1: " + str((len(path))//2))
    print("p2: " + str(count))
    

proc_file("test_input1.txt")
proc_file("test_input2.txt")
proc_file("test_input3.txt")
proc_file("test_input4.txt")
proc_file("input1.txt")
