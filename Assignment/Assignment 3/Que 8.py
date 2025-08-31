# Predefined userid and password
correct_userid = "admin"
correct_password = "1234"

# Prompt user for userid and password
userid = input("Enter User ID: ")
password = input("Enter Password: ")

if userid == correct_userid and password == correct_password:
    # Generate a random 4-digit number (captcha)
    captcha = random.randint(1000, 9999)
    print("Captcha:", captcha)
    
    # Ask user to re-enter the captcha
    entered_captcha = input("Enter the captcha shown above: ")
    
    if entered_captcha == str(captcha):
        print("Login Successful! ✅")
    else:
        print("Login Failed: Incorrect captcha ❌")
else:
    print("Login Failed: Invalid User ID or Password ❌")