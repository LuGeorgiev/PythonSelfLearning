import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_str(self):
        return f'X:{self.x}, Y:{self.y} '


class Segment:
    def __init__(self, point_1: Point, point_2: Point):
        self.point_1 = point_1
        self.point_2 = point_2
        self.distance = self.calculate_distance()

    def calculate_distance(self):
        side_a = abs(self.point_1.x - self.point_2.x)
        side_b = abs(self.point_1.y - self.point_2.y)
        side_c = math.sqrt(side_a ** 2 + side_b ** 2)
        return side_c

    def to_str(self):
        return f'{self.distance:.3f}\n({self.point_1.x}, {self.point_1.y})\n({self.point_2.x}, {self.point_2.y})'


def point_factory(x_int, y_int):
    return Point(x_int, y_int)


lines = int(input())
points = []
for line in range(lines):
    #x, y = list(map(int, input().split()))
    x, y = [int(num) for num in input().split()]
    point = point_factory(x, y)
    points.append(point)

segments = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        segment = Segment(points[i], points[j])
        segments.append(segment)

for segment in sorted(segments, key=lambda z: z.distance):
    print(segment.to_str())
    break

#for point in points:
#    print(point.to_str())