import re

def snake_camel(s):
    words = s.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

s = input("snake string:")
print(snake_camel(s))