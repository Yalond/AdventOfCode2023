
def calc(times, distances):
    grand_total = 1
    for i in range(len(times)):
        time = times[i]
        race_distance = distances[i]
        total = 0
        for time_held in range(time):
            distance_traveled = time_held * (time - time_held)
            if distance_traveled > race_distance: total += 1
        print(total)
        grand_total *= total
        total = 0
    return grand_total
 
def part1(g):
    print(g)
    times =[int (x) for x in [x.strip() for x in g[0].split(" ") if x != ""][1:]]
    distances =[int (x) for x in [x.strip() for x in g[1].split(" ") if x != ""][1:]]
    print(times)
    print(distances)
    return calc(times, distances)

def part2(g):
    print(g)
    times = [int("".join([(x) for x in [x.strip() for x in g[0].split(" ") if x != ""][1:]]))]
    distances =[int("".join([(x) for x in [x.strip() for x in g[1].split(" ") if x != ""][1:]]))]
    print(times)
    print(distances)
    return calc(times, distances)

 
       




print("part1 test: " + str(part1(open("input_test.txt", "r").readlines())))
print("part1: " + str(part1(open("input1.txt", "r").readlines())))
print("part2 test: " + str(part2(open("input_test.txt", "r").readlines())))
print("part2: " + str(part2(open("input1.txt", "r").readlines())))