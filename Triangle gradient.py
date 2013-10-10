# This program will draw a triangle gradient.

# Triangle gradient is an equilateral triangle with dots called R G and
# B (symbolise the colours) dots in it's apexes and filled with gradients
# between apexes.

# Imports area
import math

# Constants area

pi = 3.14159265359


#
# FUNCTIONS AREA
#

# Calculating the crossing point of 2 lines

def crossing_point(l1,l2):
    """crossing_point(list of dict, list of dict) -> dict

    Returns the coordinates of the point where line1 crosses line2.
    
    >>> crossing_point(RG,RB)
    {'x':0.0,'y':0.0}
    >>> crossing_point(RG,GB)
    {'x': 115.47005383792745, 'y': 100.0}
    """

    d = (l2[1]['y'] - l2[0]['y']) * (l1[1]['x'] - l1[0]['x']) - (l2[1]['x'] - l2[0]['x']) * (l1[1]['y'] - l1[0]['y'])
    a = (l2[1]['x'] - l2[0]['x']) * (l1[0]['y'] - l2[0]['y']) - (l2[1]['y'] - l2[0]['y']) * (l1[0]['x'] - l2[0]['x'])

    # Calculating the coordinates of crossing point.

    x = l1[0]['x'] + a * (l1[1]['x'] - l1[0]['x'])/d
    y = l1[0]['y'] + a * (l1[1]['y'] - l1[0]['y'])/d

    return {'x':x, 'y':y}

# Calculation of the normal to the line

def normal(line,point):
    """normal(list of dicts, dict) -> list of dict

    Return 

# The dot will be represented as a dictionary of 2 coordinates x and y.
# The line will be represented as a list of 2 points that it cames through.

side_length = 100 / math.sin(pi /3)
R = {'x' : 0, 'y' : 0}
G = {'x' : side_length * math.sin(pi / 6), 'y' : side_length * math.sin(pi / 3)}
B = {'x' : side_length * math.sin(pi / 6) * 2, 'y' : 0}

RG = [R, G]
RB = [R, B]
GB = [G, B]
                                                                                   
# Firstly we need to define percentage proximity of every dot in the triangle
# to triangle's apexes.



# R_height G_height and B_height will be the dots where heights from
# R G and B dots to the opposite sides of the triangle.

height_length = side_length * math.cos(math.radians(30))
R_height = height_length
G_height = height_length
B_height = height_length




