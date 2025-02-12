import math

def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)

degrees = float(input("Input degree: "))
radians = degrees_to_radians(degrees)
print(f"Output radian: {radians:.6f}")

def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))
area = trapezoid_area(base1, base2, height)
print(f"Expected Output: {area:.1f}")

def regular_polygon_area(n, s):
    return (n * s ** 2) / (4 * math.tan(math.pi / n))
n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))
area = regular_polygon_area(n, s)
print(f"The area of the polygon is: {area:.1f}")

def area_polygon(length, heigh):
    return length * heigh
length=int(input("Length of base: "))
heigh=int(input("Height of parallelogram: "))
area= area_polygon(length, heigh)
print(f"Expected Output: {area:.1f}")