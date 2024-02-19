neighbours = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, -1), (-1, 1), (1, 1), (-1, -1)]

def isSymbol(x): return (not x.isdigit()) and (not x == ".")

def getItemAtPos(board, pos): 
    try: return board[pos[0]][pos[1]]
    except: return "."

def posNearSymbol(board, pos):
    for neighbour in neighbours:
        newPos = (pos[0] + neighbour[0], pos[1] + neighbour[1])
        if isSymbol(getItemAtPos(board, newPos)): return True
    return False

def getGearsNearPos(board, pos):
    symbols = []
    for neighbour in neighbours:
        newPos = (pos[0] + neighbour[0], pos[1] + neighbour[1])
        if getItemAtPos(board, newPos) == "*": symbols.append(newPos)
    return symbols

def getNumberValue(board, numStartPos):
    currentNum = ""
    nearSymbol = False
    for i in range(len(board[0])):
        p = (numStartPos[0], numStartPos[1] + i)
        itemAtPos = getItemAtPos(board, p)
        if (itemAtPos.isdigit()):
            if posNearSymbol(board, p): nearSymbol = True
            currentNum += itemAtPos
        else: break
    if (nearSymbol): return (currentNum, len(currentNum))
    else: return (0, len(currentNum))

def countPartNumbers(schematic):
    total = 0
    for row in range(len(schematic)):
        col = 0
        while col < len(schematic[0]):
            if getItemAtPos(schematic, (row, col)).isdigit():
                numVal, incrementAmount = getNumberValue(schematic, (row, col))
                total += int(numVal)
                col += (incrementAmount - 1)
            col += 1
    return total

def getGearsNearNumber(board, numStartPos):
    currentNum = ""
    currentPos = numStartPos
    gearsNearNumber = []
    while True:
        itemAtPos = getItemAtPos(board, currentPos)
        if (itemAtPos.isdigit()):
            gearsNearNumber += getGearsNearPos(board, currentPos)
            currentNum += itemAtPos
        else: break
        currentPos = (currentPos[0], currentPos[1] + 1)
    return (currentNum, len(currentNum), list(set(gearsNearNumber)))

def getGearRatios(schematic):

    gearList: dict[tuple[int, int],list[int]] = {}

    for row in range(len(schematic)):
        col = 0
        while col < len(schematic[0]):
            if getItemAtPos(schematic, (row, col)).isdigit():
                num, numLen, nearGears = getGearsNearNumber(schematic, (row, col))
                for gear in nearGears:
                    if gear not in gearList: gearList[gear] = []
                    gearList[gear].append(int(num))
                col += (numLen - 1)
            col += 1
    return sum([x[0] * x[1] for x in filter(lambda x: len(x) == 2, gearList.values())])

print("Test 1: " + str(countPartNumbers([list(x.strip()) for x in open("input_test.txt", "r").readlines()])))
print("Part 1: " + str(countPartNumbers([list(x.strip()) for x in open("input1.txt", "r").readlines()])))
print("Test 2: " + str(getGearRatios([list(x.strip()) for x in open("input_test.txt", "r").readlines()])))
print("Part 2: " + str(getGearRatios([list(x.strip()) for x in open("input1.txt", "r").readlines()])))