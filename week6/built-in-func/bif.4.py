import math
import time

def square(num, delay):
    ds = delay / 1000.0
    time.sleep(ds)
    return math.sqrt(num)

n = int(input())
milis = int(input())
print(f"Square root of {n} after {milis} miliseconds is {square(n, milis)}")