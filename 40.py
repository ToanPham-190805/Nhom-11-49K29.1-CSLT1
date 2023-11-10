# Read the lengths of the sides from the user
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Check the type of triangle
if side1==side2+side3 or side2==side1+side3 or side3==side1+side2:
    print('This is not a triangle')
elif side1 == side2 == side3:
    print("This is an equilateral triangle.")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("This is an isosceles triangle.")
else:
    print("This is a scalene triangle.")
