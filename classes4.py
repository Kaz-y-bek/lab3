import math

class Point:
    def __init__(self, x1, y1):
        self.x = x1
        self.y = y1
    
    def show(self):
        print(f"Point({self.x}, {self.y})")
    
    def move(self, x2, y2):
        self.x = x2
        self.y = y2
    
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
p1 = Point(1,2)
p2 = Point(3,4)
p1.show()
print(p1.dist(p2))