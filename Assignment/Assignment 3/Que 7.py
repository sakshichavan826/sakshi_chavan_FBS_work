# Program to check if user has entered correct userid and password

# Stored correct userid and password
correct_userid = "admin"
correct_password = "1234"

userid = input("Enter userid: ")
password = input("Enter password: ")


if userid == correct_userid and password == correct_password:
    print("Login Successful! ✅")
else:
    print("Login Failed! ❌ Invalid userid or password.")