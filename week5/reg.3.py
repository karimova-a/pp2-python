import re
def low(s):
    return re.findall(r"[a-z]+(?:_[a-z]+)*", s)

s = input()
print(low(s))