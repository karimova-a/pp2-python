def up_low_letters(s):
    upper_let = sum(1 for i in s if i.isupper())
    lower_let = sum(1 for i in s if i.islower())
    return upper_let, lower_let

s = input()
up, low = up_low_letters(s)
print("upper:", up)
print("lower:", low)