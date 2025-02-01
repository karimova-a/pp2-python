def ounce(gram):
    ounces = 28.3495231 * gram
    return ounces

x = float(input())
print(f"{x} grams is equal to {ounce(x):.3f} ounces")