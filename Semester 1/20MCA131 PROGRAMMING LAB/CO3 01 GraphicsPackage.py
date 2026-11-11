# Importing specific functions from the graphics package
from graphics.circle import circle_area, circle_perimeter
from graphics.rectangle import rect_area, rect_perimeter
from graphics.cuboid import cuboid_area, cuboid_perimeter

# 1. Circle Operations
r = int(input("Enter radius of circle: "))
print("Circle Area:", circle_area(r))
print("Circle Perimeter:", circle_perimeter(r))
print()

# 2. Rectangle Operations
l = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))
print("Rectangle Area:", rect_area(l, b))
print("Rectangle Perimeter:", rect_perimeter(l, b))
print()

# 3. Cuboid Operations
l = int(input("Enter length of cuboid: "))
b = int(input("Enter breadth of cuboid: "))
h = int(input("Enter height of cuboid: "))
print("Cuboid Area:", cuboid_area(l, b, h))
print("Cuboid Perimeter:", cuboid_perimeter(l, b, h))