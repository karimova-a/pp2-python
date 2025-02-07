def pol(s):
    s = s.replace(" ", "")
    s.lower()

    if s == s[::-1]:
        return "It is polindrome"
    else:
        return "It's not polindrome"

st = input("Word:")
print(pol(st))