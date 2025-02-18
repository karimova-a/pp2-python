import math

class Pol:
    def __init__(self, sides, length):
        self.sides = sides
        self.length = length
    
    def area(self):
        return (self.sides * pow(self.length, 2)) / (4 * math.tan(math.pi / self.sides))
    
sides, length = map(int, input().split())
polygon = Pol(sides,length)
print(f"Polygon area:{polygon.area():.1f}")