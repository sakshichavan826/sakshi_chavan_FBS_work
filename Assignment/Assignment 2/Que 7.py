# program to find sum of three digit

num = int(input("Enter a three-digit number: "))

# extract digits
digit1 = num // 100          # hundreds place
digit2 = (num // 10) % 10    # tens place
digit3 = num % 10            # units place


digit_sum = digit1 + digit2 + digit3


print("The sum of the three digits is:", digit_sum)