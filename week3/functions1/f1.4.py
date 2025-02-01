def filter_prime(numbers):
    new_numbers = []

    for i in numbers:
        if i < 2 :
            continue 

        f = True
        for j in range(2, (int(i**0.5) + 1)):
            if i % j == 0 :
                f = False
                break
        if f :
            new_numbers.append(i)

    return new_numbers 


nums = []
n = int(input("List length:"))
for i in range(n):
    el = int(input())
    nums.append(el)


print(filter_prime(nums))


