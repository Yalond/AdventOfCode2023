def winningCount(x):
    winning_str, chances_str = x[x.find(":") + 1:].split("|")
    winning = set([x.strip() for x in winning_str.split()])
    return len([x for x in chances_str.split() if x.strip() in winning])

def points(x): return int(2 ** (winningCount(x) - 1))

def copies(gameList, counts):
    if len(gameList) == 1: return 1
    if len(counts) == 0: counts = [1]
    for i in range(winningCount(gameList[0])):
        if (i + 1) >= len(counts): counts.append(1)
        counts[i + 1] += counts[0]
    return counts[0] + copies(gameList[1:], counts[1:])

def copies_it(gameList, counts):
    counts = [1 for x in range(len(gameList))]
    for g in range(len(gameList)):
        for i in range(winningCount(gameList[g])):
            counts[g + i + 1] += counts[g]
    return sum(counts)

print("part1 test: " + str(sum([points(x.strip()) for x in open("input_test.txt", "r").readlines()])))
print("part1: " + str(sum([points(x.strip()) for x in open("input1.txt", "r").readlines()])))

print("part2 test: " + str(copies(open("input_test.txt", "r").readlines(), [])))
print("part2: " + str(copies(open("input1.txt", "r").readlines(), [])))

print("part2 test: " + str(copies_it(open("input_test.txt", "r").readlines(), [])))
print("part2: " + str(copies_it(open("input1.txt", "r").readlines(), [])))



