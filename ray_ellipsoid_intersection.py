# ray_ellipsoid_intersection.py
#
# Usage: python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z
# This script calculates the intersection point of a ray with the Earth reference ellipsoid.
# Parameters:
# d_l_x: x-component of origin-referenced ray direction
# d_l_y: y-component of origin-referenced ray direction
# d_l_z: z-component of origin-referenced ray direction
# c_l_x: x-component offset of ray origin
# c_l_y: y-component offset of ray origin
# c_l_z: z-component offset of ray origin
# Output:
# The script outputs the x, y, and z coordinates of the intersection point
#
# Written by Michael Hoffman
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

import sys  # argv
import math

# Constants
R_EQUATORIAL = 6378.137  # Earth’s equatorial radius in km
R_POLAR = 6356.7523  # Earth’s polar radius in km

# Helper functions

def ellipsoid_intersection(d_l, c_l):

    d_x = d_l[0] / (R_EQUATORIAL**2)
    d_y = d_l[1] / (R_EQUATORIAL**2)
    d_z = d_l[2] / (R_POLAR**2)

    c_x = c_l[0] / (R_EQUATORIAL**2)
    c_y = c_l[1] / (R_EQUATORIAL**2)
    c_z = c_l[2] / (R_POLAR**2)

    a = d_x**2 + d_y**2 + d_z**2
    b = 2 * (d_x * c_x + d_y * c_y + d_z * c_z)
    c = c_x**2 + c_y**2 + c_z**2 - 1

    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        return None  

    # Calculate the two potential intersections
    t1 = (-b - math.sqrt(discriminant)) / (2 * a)
    t2 = (-b + math.sqrt(discriminant)) / (2 * a)

    # Select the intersection closest to the ray origin
    t = t1 if t1 > 0 else t2

    if t < 0:
        return None  

    x = c_l[0] + t * d_l[0]
    y = c_l[1] + t * d_l[1]
    z = c_l[2] + t * d_l[2]

    return [x, y, z]

if len(sys.argv) != 7:
    print("Usage: python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z")
    sys.exit(1)

d_l_x = float(sys.argv[1])
d_l_y = float(sys.argv[2])
d_l_z = float(sys.argv[3])
c_l_x = float(sys.argv[4])
c_l_y = float(sys.argv[5])
c_l_z = float(sys.argv[6])

d_l = [d_l_x, d_l_y, d_l_z]
c_l = [c_l_x, c_l_y, c_l_z]

# Find intersection
intersection = ellipsoid_intersection(d_l, c_l)

# Output 
if intersection:
    print(intersection[0])  # x-component of intersection point
    print(intersection[1])  # y-component of intersection point
    print(intersection[2])  # z-component of intersection point
else:
    print("No intersection with the ellipsoid.")
