import math
import random
#1
def ounce(gram):
    ounces = 28.3495231 * gram
    return ounces

#2
def cent(fahr):
    cent = (5 / 9) * (fahr - 32)
    return cent

#3
def solve(numheads, numlegs):
    numrabbit = (numlegs - (2 * numheads)) / 2 
    numchicken = numheads - numrabbit
    print(f"Number of rabbits: {numrabbit} . Number of chickens {numchicken}")

#4
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

#5
def stringg(s):
    if len(s) == 1:
        return [s]
    permut = []
    for i in range(len(s)):
        current = s[i]
        news = s[:i] + s[i+1:]
        for next in stringg(news):
            permut.append(current + next)
    return permut

#6
def reversing():
    strin = input("Enter:")
    words = strin.split()
    result = words[::-1]
    result1 = ' '.join(result)
    return result1

#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

#8
def spy_game(nums):
    find = [0,0,7]
    for num in nums:
        if num == find[0]:
            find.pop(0)
        if not find:
            return True
    return False

#9
def volume(r):
    vol = (4/3) * math.pi * (r**3)
    return vol

#10
def unique(nums):
    new = []
    for i in nums:
        if i not in new:
            new.append(i)
    return new

#11
def pol(s):
    s = s.replace(" ", "")
    s.lower()
    if s == s[::-1]:
        return "It is polindrome"
    else:
        return "It's not polindrome"
    
#12
def histogram(nums):
    for i in nums:
        print('*' * i)

#13
def guess():
    to_guess = random.randint(1,20)
    name = input("Hello! What is your name?")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    attempts = 0
    while True:
        inp = int(input("Take a guess."))
        attempts += 1
        if inp < to_guess:
            print("Your guess is too low.")
        elif inp > to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break  