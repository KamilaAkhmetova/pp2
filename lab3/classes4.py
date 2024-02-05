class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(str(self.x) + ";" + str(self.y))

    def move(self):
        self.x = int(input("Change x: "))
        self.y = int(input("Change y: "))

    def dist(self, other_point):
        distance = ((self.x - other_point.x)**2 + (self.y - other_point.y)**2)**0.5
        return distance

x1 = float(input())
y1 = float(input())
point1 = Point(x1, y1)
point1.show()
point1.move()

x2 = float(input())
y2 = float(input())
point2 = Point(x2, y2)
point2.show()

distance_result = point1.dist(point2)
print("Distance between the two points:", distance_result)
