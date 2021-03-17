x = (elem / 10000000 for elem in range(1, 100000000) if elem % 10000000 == 0)

print(x)

# print(list(x))

for e in x:
    print(e)
