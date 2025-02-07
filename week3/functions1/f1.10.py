def unique(nums):
    new = []
    for i in nums:
        if i not in new:
            new.append(i)
    
    return new

nums = []
n = int(input("List length:"))
for i in range(n):
    el = int(input())
    nums.append(el)

print(unique(nums))