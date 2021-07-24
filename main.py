import math
import cmath
#Problem 1 Homework OOP

#Distance and Slope of two coordinates

class Line:
    def __init__(self,coor1, coor2):
        self.coor1 =coor1
        self.coor2 = coor2

    def distance(self):
        x2 = self.coor2[0]
        x1 = self.coor1[0]
        y2 = self.coor2[1]
        y1 = self.coor1[1]

        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def slop(self):
        x2 = self.coor2[0]
        x1 = self.coor1[0]
        y2 = self.coor2[1]
        y1 = self.coor1[1]

        return ((y2-y1) / (x2-x1))

coordinate1 = (3,2)
coordinate2 = (8,10)

l1 = Line(coordinate1, coordinate2)

print(l1.distance())
print(l1.slop())
