import math

def multiply(nums):
    return math.prod(nums)

n = int(input())
nums = []
for i in range(n):
    el = int(input())
    nums.append(el)

print("Product:", multiply(nums))