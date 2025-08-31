# program to calculate profit or loss

cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))
if sp > cp:
    print("Profit =", sp - cp)
else:
    print("Loss =", cp - sp)
