def reversing():
    strin = input("Enter:")
    words = strin.split()
    result = words[::-1]
    result1 = ' '.join(result)

    return result1

print(reversing())