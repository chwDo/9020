class Point:
    def __init__(self, *args):
        if len(args) == 0:
            self.x = 0
            self.y = 0
        elif len(args) == 1 or len(args) > 2:
            raise PointError('Cannot create point.')
        else:
            self.x = args[0]
            self.y = args[1]
    # REPLACE PASS ABOVE WITH YOUR CODE


class PointError(Exception):
    pass


# Will be tested only when passing no, one or two arguments,
# that have to be named; moreover, when an argument is passed,
# it will be a Point object.
class NonVerticalLine:
    def __init__(self, *, point_1=None, point_2=None):
        if point_1 is None and point_2 is None or point_1 == point_2:
            raise NonVerticalLineError('Cannot create nonvertical line.')
        elif point_1 is None:
            point_1 = Point(0, 0)
        elif point_2 is None:
            point_2 = Point(0, 0)
        self.point_1 = point_1
        self.point_2 = point_2
        if self.point_2.x == self.point_1.x:
            raise NonVerticalLineError('Cannot create nonvertical line.')
        self.slope = (self.point_2.y - self.point_1.y) / (self.point_2.x - self.point_1.x)
        self.intercept = (self.point_2.y - self.slope * self.point_2.x)

    # REPLACE PASS ABOVE WITH YOUR CODE
    def change_point_or_points(self, **kwargs):
        if len(kwargs) == 0:
            return
        if len(kwargs) > 2:
            raise NonVerticalLineError('Cannot perform this change.')
        else:
            if 'point_1' in kwargs.keys():
                self.point_1 = kwargs['point_1']
            if 'point_2' in kwargs.keys():
                self.point_2 = kwargs['point_2']
            if self.point_2.x == self.point_1.x:
                raise NonVerticalLineError('Cannot perform this change.')
            else:
                self.slope = (self.point_2.y - self.point_1.y) / (self.point_2.x - self.point_1.x)
                self.intercept = (self.point_2.y - self.slope * self.point_2.x)

class NonVerticalLineError(Exception):
    pass





NonVerticalLine(Point(), point_2=Point(3, 5))

# p1 = Point(1, 2)
# p2 = Point(4, 4)
# p3 = Point(1,5)
# p4 = Point(6,2)
# line = NonVerticalLine(point_1=p1, point_2=p2)
# print(line.point_1.x, line.point_1.y, line.point_2.x, line.point_2.y)
# print(line.slope)
# print(line.intercept)
# line.change_point_or_points(point_2=p4)