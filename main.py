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


p = Point(1,2)
d = Point(p)

