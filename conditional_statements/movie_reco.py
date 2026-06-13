user = {
    "omkar": "1234",
    "aditya": "1122",
    "prithvi": "2244"
}

movies = {
    "horror": ["AAA", "BBB", "CCC"],
    "action": ["aaa", "bbb", "ccc"],
    "comedy": ["QQQ", "WWW", "RRR"]
}

username = input("Enter the username: ")
password = input("Enter the password: ")

if username in user and user[username] == password:
    print("Login Successful!")

    movietype = input("Enter movie genre (horror/action/comedy): ")

    if movietype in movies:
        print("Available Movies:" , movies[movietype])
    else:
        print("Invalid movie genre")
else:
    print("Invalid username or password")