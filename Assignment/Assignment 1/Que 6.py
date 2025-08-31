# program to find  third angle of triangle

angle1 = float(input("Enter first angle of triangle: "))
angle2 = float(input("Enter second angle of triangle: "))

# Sum of angles of a triangle is always 180
angle3 = 180 - (angle1 + angle2)

# Display result
print("The third angle of the triangle is:", angle3)



