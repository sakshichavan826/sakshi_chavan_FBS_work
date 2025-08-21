
L = float(input("Enter length of rectangle: "))
B = float(input("Enter breadth of rectangle: "))
r = float(input("Enter radius of semicircle: "))

# Area calculation
area = (L * B) + (0.5 * 3.14 * r * r)

# Perimeter calculation
perimeter = (2 * L + B) + (3.14 * r)

# Output
print("Area of figure =", area)
print("Perimeter of figure =", perimeter)