import math

def area(r):
    return math.pi * (r**2)

radii = [2, 5, 7.1, 0.3, 10]

areas = []
for r in radii:
    a = area(r)
    areas.append(a)

print(areas)
# >>> [12.566370614359172, 78.53981633974483, 158.36768566746147, 0.2827433388230814, 314.1592653589793]
