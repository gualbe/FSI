from functools import reduce

data = [2, 3, 5, 7]
multiplier = lambda x, y: x*y

# Method 1 (loop)
res = 1
for x in data:
    res = multiplier(res, x)
print(res)

# Method 2 (reduce)
res = reduce(multiplier, data)
print(res)

