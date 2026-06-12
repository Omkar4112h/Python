user = {"Omkar":"1234",
        "Aditya":"5678",
        "Prithvi":"9101"}
username = input("Enter your username: ")
password = input("Enter your password: ")
if username in user and user[username] == password:
    print("Login successful")
else:
    print("Invalid username or password")