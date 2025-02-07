def stringg(s):
    if len(s) == 1:
        return [s]
    
    permut = []
    for i in range(len(s)):
        current = s[i]
        news = s[:i] + s[i+1:]
        for next in stringg(news):
            permut.append(current + next)
    
    return permut


str = input("Enter a word:")

for i in stringg(str):
    print(i)
