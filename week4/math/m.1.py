import math
def convert_to_rad(degree):
    return math.radians(degree)

degree = int(input("Input degree:"))
print(f"Radian:{convert_to_rad(degree):.6f}")