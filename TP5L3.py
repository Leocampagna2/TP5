import math
from math import atan2
class Point:
    def __init__(self, *args):
        if len(args) == 2:
            self.x = args[0]
            self.y = args[1]
        elif len(args) == 1:
            self.x = args[0].x
            self.y = args[0].y
        elif len(args) == 0:
            self.x = 0
            self.y = 0

    def __getitem__(self, p):
        if p == 0:
            return self.x
        elif p == 1:
            return self.y
        else:
            raise IndexError('mauvais index')

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def __eq__(self,a):
        return (self.x == a.x) and (self.y == a.y)

    def angle(self, p):
        return math.degrees(math.atan2(p.y-self.y, p.x-self.x))

    def distance_point(self,p):
        return math.sqrt((p.x-self.x)**2+(p.y-self.y)**2)

p = Point(1, 2)
t = Point(3, 4)
print(p)
d = Point(p)
print(p == Point(1,2))
print(t.angle(p))
print(t.distance_point(p))