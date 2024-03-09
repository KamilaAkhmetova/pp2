import math

def area_of_regular_polygon(num_sides, side_length):
   return (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))

num_sides = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))

area = area_of_regular_polygon(num_sides, side_length)
print("The area of the polygon is:", area)