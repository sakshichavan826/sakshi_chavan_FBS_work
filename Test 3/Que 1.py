n = int(input("Enter how many prime numbers to print: "))
count = 0   # how many prime found
num = 2     # number to check for prime

while count < n:
    # check if num is prime
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")
        count += 1

    num += 1