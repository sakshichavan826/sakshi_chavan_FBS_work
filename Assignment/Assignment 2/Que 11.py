# Program to calculate the minimum number of notes needed for an amount

# Input amount
amount = int(input("Enter the amount: "))

# List of available notes (you can adjust according to the currency)
notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

print("Minimum number of notes:")

for note in notes:
    if amount >= note:
        count = amount // note   # Number of notes of this denomination
        amount = amount % note   # Remaining amount
        print(f"{note} : {count}")