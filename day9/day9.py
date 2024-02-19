import re

def calculate(steps):
    while any(steps[-1]): steps.append([b - a for a, b in zip(steps[-1], steps[-1][1:])])
    steps.reverse()
    steps[0].append(0)
    for step, last_step in zip(steps[1:], steps): step.append(step[-1] + last_step[-1])
    return steps[-1][-1]

parts = [list(map(int, re.findall(r'-?\w+', row))) for row in open("input1.txt", "r")]
print(f'p1: {sum([calculate([x]) for x in parts])}')
print(f'p2: {sum([calculate([list(reversed(x))]) for x in parts])}')