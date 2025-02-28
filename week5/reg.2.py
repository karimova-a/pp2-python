import re

def a_tt_b(s):
    return re.findall(r"ab{2,3}", s)

s = input()
print(a_tt_b(s))