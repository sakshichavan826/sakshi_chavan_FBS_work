 # program to find roots of quadratic equation

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate discriminant
d = (b**2) - (4*a*c)

root1 = (-b + cmath.sqrt(d)) / (2*a)
root2 = (-b - cmath.sqrt(d)) / (2*a)

print("The roots of the quadratic equation are:")
print("Root 1 =", root1)
print("Root 2 =", root2)