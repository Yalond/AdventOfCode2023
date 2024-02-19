
def get_pair(p1, p2):
    if (p1[0] < p2[0]): return (p1, p2)
    elif (p1[0] > p2[0]): return (p2, p1)
    elif (p1[1] > p2[1]): return (p1, p2)
    else: return (p2, p1)

def proc(filename, expanded):

    grid = []

    expanded_rows = []
    expanded_cols = []

    for line in open(filename, "r").readlines():
        expanded_rows.append("M" if all(x == "." for x in line.strip()) else ".")
        grid.append(list(line.strip()))

    for col in range(len(grid[0])):
        if all(grid[row][col] == "." for row in range(len(grid))): expanded_cols.append("M")
        else: expanded_cols.append(".")

    count = 0
    positions_map = []
    for i, row in enumerate(grid):
        for j, symbol in enumerate(row):
            if symbol == "#":
                row[j] = count
                positions_map.append((count, (i, j)))
                count += 1

    total = 0
    seen_lengths = set()

    for i1, p1 in enumerate(positions_map):
        for i2, p2 in enumerate(positions_map):
            if i1 == i2: continue

            p1r, p1c = p1[1]
            p2r, p2c = p2[1]

            start_row = min(p1r, p2r)
            end_row = max(p1r, p2r)
            start_col = min(p1c, p2c)
            end_col = max(p1c, p2c)

            row_dist = sum([expanded if expanded_rows[i] == "M" else 1 for i in range(start_row, end_row)])
            col_dist = sum([expanded if expanded_cols[i] == "M" else 1 for i in range(start_col, end_col)])

            pair = get_pair(p1[1], p2[1])
            if pair not in seen_lengths:
                seen_lengths.add(pair)
                total += row_dist + col_dist
    return total

print(f'p1: {proc("input1.txt", 2)} p2: {proc("input1.txt", 1000000)}')
    
