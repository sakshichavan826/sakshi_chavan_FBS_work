# program to calculate selling price of book

cost_price = float(input("Enter cost price of book: "))
discount_percent = float(input("Enter discount percentage: "))


discount = (discount_percent / 100) * cost_price

selling_price = cost_price - discount

print("Selling Price of the book is:", selling_price)