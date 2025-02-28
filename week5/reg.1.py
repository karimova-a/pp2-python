import re

def a_to_b(s):
    return re.findall(r"ab*", s)

s = input()
print(a_to_b(s))