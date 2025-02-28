import re
 
def oneup(s):
    return re.findall(r"[A-Z]{1}[a-z]+", s)

s = input()
print(oneup(s))