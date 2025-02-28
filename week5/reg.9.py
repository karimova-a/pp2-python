import re

def repl_s(s):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', s)

s = input()
print(repl_s(s))