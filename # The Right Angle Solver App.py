# The Right Angle Solver App
import math
print("Welcome to the Right Triangle Solver App")
side_a = float(input("\nWhat is the length of the first leg of the triangle? "))
side_b = float(input("\nWhat is the length of the second leg of the triangle? "))

side_c = math.sqrt(side_a**2 + side_b**2)
side_c = round(side_c, 3)

area = 0.5*side_a*side_b
area = round(area, 3)
print(f"\nFor a triangle with legs of {side_a}, {side_b}, the hypotenuse is {side_c}, and the area is {area}")
exit
