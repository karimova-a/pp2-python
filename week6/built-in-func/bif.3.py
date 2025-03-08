def palindrome(s):
    ss = s.replace(" ", "").lower()
    return ss == ss[::-1]

s = input()
print(palindrome(s))