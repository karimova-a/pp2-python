import math

class Par:
    def __init__(self, length, height):
        self.length = length
        self.height = height
    
    def area(self):
        return self.length * self.height
    
base, height = map(int, input().split())
parallelogram = Par(base, height)
print(f"Parallelogram area:{parallelogram.area():.1f}")
