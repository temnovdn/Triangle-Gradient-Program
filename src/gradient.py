
from point import Point
from math import sqrt


class TriangleGradient:
    def __init__(self, red_apex, green_apex, blue_apex):
        """
        :param Point red_apex:
        :param Point green_apex:
        :param Point blue_apex:
        """
        self.red_apex = red_apex
        self.green_apex = green_apex
        self.blue_apex = blue_apex

        self.red_scale = max(spline_length(red_apex, green_apex), spline_length(red_apex, blue_apex))
        self.green_scale = max(spline_length(green_apex, red_apex), spline_length(green_apex, blue_apex))
        self.blue_scale = max(spline_length(blue_apex, green_apex), spline_length(blue_apex, red_apex))

        self.internal_points = self.create_points_list()

    def create_points_list(self):
        """

        :return: a list of points
        """
        points = []
        x_min = min(self.red_apex.x, self.green_apex.x, self.blue_apex.x)
        x_max = max(self.red_apex.x, self.green_apex.x, self.blue_apex.x)
        y_min = min(self.red_apex.y, self.green_apex.y, self.blue_apex.y)
        y_max = max(self.red_apex.y, self.green_apex.y, self.blue_apex.y)

        for x in range(x_min, x_max + 1, 1):
            for y in range(y_min, y_max + 1, 1):
                point = Point(x, y)

                a = (self.red_apex.x - point.x) * (self.green_apex.y - self.red_apex.y) - (self.green_apex.x - self.red_apex.x) * (self.red_apex.y - point.y)
                b = (self.green_apex.x - point.x) * (self.blue_apex.y - self.green_apex.y) - (self.blue_apex.x - self.green_apex.x) * (self.blue_apex.y - point.y)
                c = (self.blue_apex.x - point.x) * (self.red_apex.y - self.blue_apex.y) - (self.red_apex.x - self.blue_apex.x) * (self.green_apex.y - point.y)

                if (a >= 0 and b >= 0 and c >= 0) or (a <=0 and b <= 0 and c <= 0):
                    point.red = int(round((spline_length(self.red_apex, point) / self.red_scale) * 255, 0))
                    point.green = int(round((spline_length(self.green_apex, point) / self.green_scale) * 255, 0))
                    point.blue = int(round((spline_length(self.blue_apex, point) / self.blue_scale) * 255, 0))
                    points.append(point)

        return points


def spline_length(point1, point2):
    """spline_length(dict,dict) -> float
    Return the length of spline between point1 and point2.
    """
    return sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)
