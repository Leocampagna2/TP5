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
        return atan2(p.y-self.y, p.x-self.x)



p = Point(1,2)
print(p)
d = Point(p)
print(p == Point(1,2))