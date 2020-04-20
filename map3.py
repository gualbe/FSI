temps = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19)]

c_to_f = lambda data: (data[0], (9/5)*data[1] + 32)

print( list(map(c_to_f, temps)) )
