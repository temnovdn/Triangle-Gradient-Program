# This program will draw a triangle gradient.

# Triangle gradient is an equilateral triangle with dots called R G and
# B (symbolise the colours) dots in it's apexes and filled with gradients
# between apexes.

# Imports area
import math

# 
# FUNCTIONS AREA
# 

# Calculating the crossing point of 2 lines

##def crossing_point(l1,l2):
##    """crossing_point(list of dict, list of dict) -> dict
##
##    Returns the coordinates of the point where line1 crosses line2.
##    
##    >>> crossing_point(RG,RB)
##    {'x':0.0,'y':0.0}
##    >>> crossing_point(RG,GB)
##    {'x': 115.47005383792745, 'y': 100.0}
##    """
##
##    d = (l2[1]['y'] - l2[0]['y']) * (l1[1]['x'] - l1[0]['x']) - (l2[1]['x'] - l2[0]['x']) * (l1[1]['y'] - l1[0]['y'])
##    a = (l2[1]['x'] - l2[0]['x']) * (l1[0]['y'] - l2[0]['y']) - (l2[1]['y'] - l2[0]['y']) * (l1[0]['x'] - l2[0]['x'])
##
##    # Calculating the coordinates of crossing point.
##
##    x = l1[0]['x'] + a * (l1[1]['x'] - l1[0]['x'])/d
##    y = l1[0]['y'] + a * (l1[1]['y'] - l1[0]['y'])/d
##
##    return {'x':x, 'y':y}

# Calculation of the normal to the line

def normal(line, first_point):
    """normal(list of dicts, dict) -> list of dict

    Return the normal to the line, coming through the first_point.
    """

    # It's obvious that first point of a normal is already known.

    second_point = {'x':0, 'y':0}

##    # Calculating direction vector for line
##
##    dir = {'x':0,'y':0}
##    dir['x'] = line[1]['x'] - line[0]['x']
##    dir['y'] = line[1]['y'] - line[0]['y']
##
##    # Calculating the parameters of line formula
##
##    k1 = (line[0]['y'] - line[1]['y']) / (line[1]['x'] - line[0]['x'])
##    b1 = (line[0]['x'] * line[1]['y'] - line[1]['x'] * line [0]['y']) / (line[1]['x'] - line[0]['x'])
##
##    # Calculating parameters of normal formula
##
##    if k1 !=0:
##        k2 = -1 / k1
##    else:
##        k2 = 1
##
##    b2 = first_point['y'] - k2 * first_point['x']
##
##    # Calculating the coordinates of second point
##
##    x2 = (b2 - b1) / (k1 - k2)
##    y2 = k2 * x2 + b2
##
##    normal = [first_point, {'x':x2, 'y':y2}]

    # Calculating a1 and c1 parameters for line formula a1*b1*x+y+c1=0

    a1 = line[0]['y'] - line[1]['y']
    b1 = line[1]['x'] - line[0]['x']
    c1 = line[0]['x'] * line[1]['y'] - line[1]['x'] * line[0]['y']

    # Normal formula will be b1*x-a1*y+c2=0. Calculating c2.

    c2 = a1 * first_point['y'] - b1 * first_point['x']

    # Calculating the crossing point coordinates

    second_point['y'] = (c2 * a1 / b1 + c1) / (a1**2 / b1 + b1)
    second_point['x'] = (a1 * second_point['y'] - c2) / b1
    
    normal = [first_point, second_point]    
    
    return normal

# Calculaion of spline length

def spline_length(point1, point2):
    """spline_length(dict,dict) -> float

    Return the length of spline between point1 and point2.

    >>>spline_length({'x':0, 'y':0}, {'x':0, 'y':1})
    1
    >>>spline_length({'x':0, 'y':0}, {'x':-1, 'y':-1})
    1.4142135623730951
    """

    return math.sqrt((point2['x'] - point1['x'])**2 + (point2['y'] + point1['y'])**2)

# The point will be represented as a dictionary of 2 coordinates x and y.
# The line will be represented as a list of 2 points that it cames through.

side_length = 100 / math.sin(math.pi / 3)
R = {'x' : 0, 'y' : 0}
G = {'x' : side_length * math.sin(math.pi / 6), 'y' : side_length * math.sin(math.pi / 3)}
B = {'x' : side_length * math.sin(math.pi / 6) * 2, 'y' : 0}

RG = [R, G]
RB = [R, B]
GB = [G, B]

# Calculating 2 points of every height in the triangle
height_R = normal(GB, R)
height_G = normal(RB, G)
height_B = normal(RG, B)

# Calculating lengths of all heights
length_R = spline_length(height_R[0], height_R[1])
length_G = spline_length(height_G[0], height_G[1])
length_B = spline_length(height_B[0], height_B[1])
                                                                                   
# Firstly we need to define percentage proximity of every dot in the triangle
# to triangle's apexes.
# To do that we'll find normals from that point to all heights and measure lengths
#
def close_R(point):
    """close_R(dict) -> number

    Return the percent of "closiness" of a point inside the triangle to R apex.
    >>> close_R(R)
    100.0
    >>> close_R(G)
    0.0
    """

    normal_to_R = normal(height_R, point)
    percent = 100 - spline_length(normal_to_R[1], R) / length_R * 100

    return percent

def close_G(point):
    """close_G(dict) -> number

    Return the percent of "closiness" of a point inside the triangle to G apex.
    >>> close_G(G)
    100.0
    >>> close_G(R)
    0.0
    """

    normal_to_G = normal(height_G, point)
    percent = 100 - spline_length(normal_to_G[1], G) / length_G * 100

    return percent

def close_B(point):
    """close_B(dict) -> number

    Return the percent of "closiness" of a point inside the triangle to B apex.
    >>> close_B(B)
    100.0
    >>> close_B(G)
    0.0
    """

    normal_to_B = normal(height_B, point)
    percent = 100 - spline_length(normal_to_B[1], B) / length_B * 100

    return percent
