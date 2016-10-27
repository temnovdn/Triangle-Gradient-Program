from gradient import *
from point import Point

triangle = TriangleGradient(Point(0,0), Point(100, 100), Point(200, 100))
for point in triangle.internal_points:
    print (point.red, point.green, point.blue)
