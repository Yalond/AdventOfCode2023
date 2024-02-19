
def process(data):
    seedNums = []
    containers = []
    currentContainer = None
    for line in data:
        if line[:5] == "seeds":
            seedNums = [int(x) for x in line.strip().split(" ")[1:]]
        elif line == "\n": 
            if (currentContainer != None): containers.append(currentContainer)
            currentContainer = []
        elif line.split(" ")[0].isdigit():
            currentContainer.append([int(x.strip()) for x in line.split(" ")])
    if len(currentContainer) > 0: containers.append(currentContainer)
    return seedNums, containers

def find_lowest_seed(initial_seeds, containers):
    seeds = initial_seeds[:]
    for container in containers:
        new_seed_values = []
        for seed in seeds:
            did_modify_seed = False
            for map_row in container:
                dest_map, source_map, range_map = map_row
                if seed >= source_map and seed < (source_map + range_map):
                    did_modify_seed = True
                    new_seed_values.append(dest_map + (seed - source_map))
            if not did_modify_seed:
                new_seed_values.append(seed)
        seeds = new_seed_values
    return min(seeds) 

def get_lowest_seed_value(seed_ranges):
    return min([x[0] for x in seed_ranges])

def get_lowest_seed_number(seed_ranges, containers):

    if len(seed_ranges) == 0: return []
    if len(containers) == 0: return get_lowest_seed_value(seed_ranges)

    lowest_seed_numbers = []
    current_container = containers[0]
    ranges = seed_ranges[:]

    while len(ranges) > 0:
        
        current_range_start, current_range_size = ranges[0]
        ranges = ranges[1:]
        valueIsInRange = False
        for dest_map_start, source_map_start, range_map in current_container:

            current_range_end = current_range_start + current_range_size
            source_map_end = source_map_start + range_map

            # seed range is totally inside available range
            if current_range_start >= source_map_start and current_range_end <= source_map_end:
                valueIsInRange = True
                new_range_start = dest_map_start + (current_range_start - source_map_start)
                lowest_seed_numbers.append(get_lowest_seed_number([[new_range_start, current_range_size]], containers[1:]))
                break 

            # seed range is not inside available range at all
            elif current_range_end <= source_map_start or current_range_start >= source_map_end:
                continue

            # seed range to left of map range but intersects
            elif current_range_start < source_map_start and current_range_end >= source_map_start and current_range_end <= source_map_end:
                valueIsInRange = True
                r1s = current_range_start # outside
                r1e = source_map_start
                r2s = source_map_start # inside
                r2e = current_range_end
                ranges.append([r1s, r1e - r1s]) # add back in overflow
                lowest_seed_numbers.append(get_lowest_seed_number([[dest_map_start + (r2s - source_map_start), r2e - r2s]], containers[1:]))
                break 

            # seed range to right of map range but intersects 
            elif current_range_start >= source_map_start and current_range_start < source_map_end:
                valueIsInRange = True
                r1s = source_map_end # outside
                r1e = current_range_end
                r2s = current_range_start # inside
                r2e = source_map_end
                ranges.append([r1s, r1e - r1s]) # add back in overflow
                lowest_seed_numbers.append(get_lowest_seed_number([[dest_map_start + (r2s - source_map_start), r2e - r2s]], containers[1:]))
                break 
            
            # map range is inside seed range
            elif current_range_start <= source_map_start and current_range_end > source_map_end:
                valueIsInRange = True
                r1s = current_range_start # outside
                r1e = source_map_start
                r2s = source_map_start # inside
                r2e = source_map_end
                r3s = source_map_end # outside
                r3e = current_range_end

                ranges.append([r1s, r1e - r1s]) # add back in overflow
                ranges.append([r3s, r3e - r3s]) # add back in overflow

                lowest_seed_numbers.append(get_lowest_seed_number([[dest_map_start + (r2s - source_map_start), r2e - r2s]], containers[1:]))
                break 

            else: print("unhandled intersection")

        if not valueIsInRange:
            lowest_seed_numbers.append(get_lowest_seed_number([[current_range_start, current_range_size]], containers[1:]))

    return min(lowest_seed_numbers)

def find_lowest_seed_ranges(initial_seeds, containers):
    seed_ranges = [[initial_seeds[i], initial_seeds[i + 1]] for i in range(0, len(initial_seeds), 2)]
    return get_lowest_seed_number(seed_ranges, containers)
 
def run(filename):
    data = open(filename, "r").readlines()
    seeds, containers = process(data)
    return find_lowest_seed(seeds, containers)

def run2(filename):
    data = open(filename, "r").readlines()
    seeds, containers = process(data)
    return find_lowest_seed_ranges(seeds, containers)

print("part1 test: " + str(run("input_test.txt")))
print("part1: " + str(run("input1.txt")))

print("part2 test: " + str(run2("input_test.txt")))
print("part2: " + str(run2("input1.txt")))
