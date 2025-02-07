import math
def volume(r):
    vol = (4/3) * math.pi * (r**3)
    return vol

radius = int(input("Enter radius:"))
print(f"The volume is:{volume(radius):.2f}")