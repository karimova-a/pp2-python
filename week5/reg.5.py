import re

def andb(s):
    return re.match(r"a.*b$", s)

s =input()


print(andb(s))