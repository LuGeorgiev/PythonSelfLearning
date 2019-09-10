import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def calc_distance(point_1, point_2):
        side_a = point_1.x - point_2.x
        side_b = point_1.y - point_2.y
        side_c = math.sqrt(side_a ** 2 + side_b ** 2)
        return side_c

    def to_str(self):
        return f'X:{self.x}, Y:{self.y} '


def point_factory(coor):
    x_int, y_int = [int(point) for point in coor.split(':')]
    return Point(x_int, y_int)


class Box:
    def __init__(self, upper_left: Point, upper_right: Point, bottom_left: Point, bottom_right: Point):
        self.upper_left = upper_left
        self.upper_right = upper_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right
        self.height = self.get_height()
        self.width = self.get_width()
        self.perimeter = self.calc_perimeter()
        self.area = self.calc_area()

    def get_width(self):
        width = Point.calc_distance(self.upper_left, self.upper_right)
        return width

    def get_height(self):
        height = Point.calc_distance(self.upper_left, self.bottom_left)
        return height

    def calc_perimeter(self):
        return self.height * 2 + self.width * 2

    def calc_area(self):
        return self.height * self.width

    def to_str(self):
        return f'Box: {self.width:.0f}, {self.height:.0f}\nPerimeter: {self.perimeter:.0f}\nArea: {self.area:.0f}'


def box_factory(u_l, u_r, b_l, b_r):
    upper_left = point_factory(u_l)
    upper_right = point_factory(u_r)
    bottom_left = point_factory(b_l)
    bottom_right = point_factory(b_r)
    return Box(upper_left, upper_right, bottom_left, bottom_right)


data_list = input().split(' | ')
box_list = []
while data_list[0] != 'end':
    box_list.append(box_factory(data_list[0], data_list[1], data_list[2], data_list[3]))
    data_list = input().split(' | ')

for box in box_list:
    print(box.to_str())