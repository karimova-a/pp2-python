import re

def camel_snake(s):
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s).lower()

s = input()
print(camel_snake(s))