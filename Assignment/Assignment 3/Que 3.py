# Program to check whether a triangle is valid based on its angles

# input three angles from the user
angle1 = float(input("Enter first angle: "))
angle2 = float(input("Enter second angle: "))
angle3 = float(input("Enter third angle: "))

# check if sum of angles is 180 and all angles are greater than 0
if (angle1 + angle2 + angle3) == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")