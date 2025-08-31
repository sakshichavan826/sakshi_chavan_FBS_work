# program  to convert distance

feet = int(input("Enter distance in feet: "))
inches = int(input("Enter distance in inches: "))

# Convert feet to inches and add
total_inches = (feet * 12) + inches

# Convert inches to centimeters
centimeters = total_inches * 2.54

# Convert to meters
meters = centimeters / 100

print("Distance in meters:", meters)
print("Distance in centimeters:", centimeters)