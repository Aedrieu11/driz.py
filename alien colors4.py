usernames = ['admin', 'jomari', 'sarah', 'mike', 'anna']

for username in usernames:
    if username == 'admin':
        print("Hello Admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")