username =str(input("Username: "))
password = str(input("Password: "))

if username == "keerthi" and password == "heyy":
    print("Login successful")
elif username != "keerthi" and password!="heyy":
    print("Login failed!")
else:
    print("Invalid username or password.Please try again!")
