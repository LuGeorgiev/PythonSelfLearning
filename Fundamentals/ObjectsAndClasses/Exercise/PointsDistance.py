import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def calculate_distance (point_1: Point, point_2: Point):
    side_a = abs(point_1.x - point_2.x)
    side_b = abs(point_1.y - point_2.y)
    return math.sqrt(side_a ** 2 + side_b ** 2)


def point_factory(x_int, y_int):
    return Point(x_int, y_int)


x_1, y_1 = list(map(int, input().split()))
x_2, y_2 = list(map(int, input().split()))

point_1 = point_factory(x_1, y_1)
point_2 = point_factory(x_2, y_2)

distance = calculate_distance(point_1, point_2)
print(f'{distance:.3f}')
