import math

def area(r):
    return math.pi * (r**2)

radii = [2, 5, 7.1, 0.3, 10]

areas = map(area, radii)

print(areas)
# <map object at 0x7f8f482b2d90>

print(list(areas))
# >>> [12.566370614359172, 78.53981633974483, 158.36768566746147, 0.2827433388230814, 314.1592653589793]
