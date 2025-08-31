x = float(input("Enter first side: "))
y = float(input("Enter second side: "))
z = float(input("Enter third side: "))
if x + y > z and x + z > y and y + z > x:
    print("Triangle is valid.")
else:
    print("Triangle is not valid.")