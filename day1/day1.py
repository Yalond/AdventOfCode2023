def calc(x):
    for i in x:
        if i.isdigit():
            return i
    
part1 = lambda s: sum([int(calc(x.strip()) + calc(x.strip()[::-1])) for x in s.readlines()])

print("Test 1: " + str(part1(open("input_test.txt", "r"))))
print("Part 1: " + str(part1(open("input1.txt", "r"))))

numStrings = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def findLocationOfStrings(xs, t=0):
    if (len(xs) == 0): return []
    if (xs[0].isdigit()): return [xs[0]] + findLocationOfStrings(xs[1:], t + 1)
    for num in numStrings:
        if len(xs) >= len(num) and xs[0:len(num)] == num:
            return [str(numStrings.index(num))] + findLocationOfStrings(xs[1:], t + len(num))
    return findLocationOfStrings(xs[1:], t + 1)

def getTotal(xs):
    a = findLocationOfStrings(xs)
    return int(a[0] + a[-1])

print("Test 2: " + str(sum([getTotal(x.strip()) for x in open("input_test2.txt", "r").readlines()])))
print("Part 2: " + str(sum([getTotal(x.strip()) for x in open("input1.txt", "r").readlines()])))



    











