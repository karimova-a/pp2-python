import math

class Trap:
    def __init__(self, height, base1,base2):
        self.height = height
        self.base1 = base1
        self.base2 = base2
    
    def area(self):
        return ((self.base1 + self.base2) / 2) * self.height

h, b1, b2 = map(int, input().split())
trapezoid = Trap(h, b1, b2)
print("Trapezoid area:", trapezoid.area())

'''def area_trap(height, base1, base2):
    return ((base1 + base2) / 2) * height

height, base1, base2 = map(int,input().split())
print(area_trap(height, base1, base2))
'''