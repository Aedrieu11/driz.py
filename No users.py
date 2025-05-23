# List of usernames
usernames = ["admin", "user1", "user2", "user3"]

if not usernames:
    print("We need to find some users!")
else:
    for username in usernames:
        if username == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")

usernames.clear()

if not usernames:
    print("We need to find some users!")