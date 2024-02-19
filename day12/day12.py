import re

def rp(xs, i, v):
    a = xs[:]
    a[i] = v
    return a

def mem_f():

    mem = dict()
    def t(a, b, f, c):
        key = str(a) + str(b) + str(c)
        if key in mem: return mem[key]
        else:
            res = proc_rec(a, b, f, c)
            mem[key] = res
            return res
    return t

def proc_rec(springs, nums, mem, counting = False):

    if "#" not in springs:
        if len(springs) == 0 and len(nums) == 0: return 1
        elif len(springs) == 0 and len(nums) == 1 and nums[0] == 0: return 1
        elif len(nums) == 0: return 1

    if "#" in springs and len(nums) == 0: return 0

    if len(springs) == 0: return 0
    if len(springs) < nums[0]: return 0

    if counting: 

        if nums[0] == 0:
            if springs[0] == ".": return mem(springs[1:], nums[1:], mem, False)
            elif springs[0] == "#": return 0
            else: return mem(rp(springs, 0, "."), nums, mem, counting)

        elif nums[0] > 0:
            if springs[0] == ".": return 0
            elif springs[0] == "#": return mem(springs[1:], rp(nums, 0, nums[0] - 1), mem, counting)
            else: return mem(rp(springs, 0, "#"), nums, mem, counting)

        else: return 0

    else:

        if springs[0] == ".": return mem(springs[1:], nums, mem, counting)
        elif springs[0] == "#": return mem(springs[1:], rp(nums, 0, nums[0] - 1), mem, True)
        else: return mem(rp(springs, 0, "."), nums, mem, False) + mem(rp(springs, 0, "#"), nums, mem, True)

def proc(line, b):
    springs, *nums_str = re.findall(r"[?|.|#]+|\d+", line)
    nums = list(map(int, nums_str))
    s = list(springs)
    g = ["?"]
    if not b: return proc_rec(s, nums, mem_f())
    else: return proc_rec(s + g + s + g + s + g + s + g + s, nums * 5, mem_f())



def p1(filename):
    print(filename)
    print(f"p1: {sum([proc(x, False) for x in open(filename, 'r').readlines()])}")
    print(f"p2: {sum([proc(x, True) for x in open(filename, 'r').readlines()])}")

p1("input_test.txt")
p1("input1.txt")