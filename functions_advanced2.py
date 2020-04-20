import math
import statistics as stat

def sd (*args):
    m = stat.mean(args)
    r = 0
    for x in args:
        r += (x - m) ** 2
    r /= len(args)
    return math.sqrt(r)

def sd2 (*args):
    m = stat.mean(args)
    r = stat.mean([(x - m) ** 2 for x in args])
    return math.sqrt(r)

res = sd(1, 2, 3)
print(res)

res = sd2(1, 2, 3)
print(res)
