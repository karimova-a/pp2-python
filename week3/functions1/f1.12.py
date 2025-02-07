def histogram(nums):
    for i in nums:
        print('*' * i)
    
nums = []
n = int(input("List length:"))
for i in range(n):
    el = int(input())
    nums.append(el)

histogram(nums)