import re

def split_upper(s):
    return re.split(r'(?=[A-Z])', s)

s = input()
print(split_upper(s))