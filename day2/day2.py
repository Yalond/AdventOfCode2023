
def parseGameSection(gameSection: str):
    sections = [x.strip() for x in gameSection.split(",")]
    return {x[1]: int(x[0]) for x in  [x.split(" ") for x in sections]}

def possibleGameNumber(game: str, reds, greens, blues) -> int:
    sections = game.split(":")
    constraint = {"red": reds, "green": greens, "blue": blues}
    for reveal in [parseGameSection(x) for x in sections[1].split(";")]:
        for color, value in reveal.items():
            if constraint[color] < value : return 0
    return int(sections[0].split(" ")[1])

def powerGameNumber(game: str) -> int:
    sections = game.split(":")
    maxValues = {"red": 1, "green": 1, "blue": 1}
    for reveal in [parseGameSection(x) for x in sections[1].split(";")]:
        for color, value in reveal.items():
            if maxValues[color] < value : maxValues[color] = value
    return maxValues["red"] * maxValues["blue"] * maxValues["green"]

def p1(fileName):
    return sum([possibleGameNumber(game.strip(), 12,13,14) for game in open(fileName, "r").readlines()])

def p2(fileName):
    return sum([powerGameNumber(game.strip()) for game in open(fileName, "r").readlines()])

print("Test part 1: " + str(p1("test_input1.txt")))
print("part 1: " + str(p1("input1.txt")))
print("Test part 2: " + str(p2("test_input1.txt")))
print("part 2: " + str(p2("input1.txt")))




