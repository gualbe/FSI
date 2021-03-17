import statistics as stat

data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

avg = stat.mean(data)

print("Mean: ", avg)

res = filter(lambda x: x > avg, data)

print(res)

print( list(res) )
