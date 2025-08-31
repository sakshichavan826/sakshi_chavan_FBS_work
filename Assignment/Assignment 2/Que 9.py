# Program to swap two numbers without using a third variable

# Input from user
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

# Swapping using arithmetic operations
a = a + b
b = a - b
a = a - b

print("After swapping:")
print("a =", a)
print("b =", b)