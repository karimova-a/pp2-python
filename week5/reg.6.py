import re

def repl(s):
    return re.sub(r'[ ., ]' , ':' , s)

s = input()
print(repl(s))