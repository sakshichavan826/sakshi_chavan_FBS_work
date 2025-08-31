# Program to check whether an alphabet is a vowel or consonant


ch = input("Enter an alphabet: ")

# Check if input is a single alphabetic character
if len(ch) == 1 and ch.isalpha():
    # Convert to lowercase for easy comparison
    ch = ch.lower()

    if ch in ['a', 'e', 'i', 'o', 'u']:
        print(f"{ch} is a vowel.")
    else:
        print(f"{ch} is a consonant.")
else:
    print("Invalid input! Please enter a single alphabetic character.")