class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

# test 1
p1 = Point(3, -2)
p2 = Point(3, -2)
points = set((p1, p2))
print(points, Point(3, -2) in points)

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))
    
    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y

p1 = Point(3, -2)
p2 = Point(3, -2)
points = set((p1, p2))
print(points, Point(3, -2) in points)