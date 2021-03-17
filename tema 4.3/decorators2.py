from time import time

def execution_time (f):
    def temp (*args):
        start = time()
        res = f(*args)
        print("Execution time: ", time() - start, " secs.")
        return res
    return temp

@execution_time
def func(n):
    s = 0
    for i in range(1, n):
        s+= i ** 2
    return s

r = func(10000000)

print("Result: ", r)
