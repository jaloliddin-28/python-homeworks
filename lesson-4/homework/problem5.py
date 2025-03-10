password = input("Create a password: ")
if password.lower() != password and len(password) >= 8:
    print("Password is strong")
elif len(password) < 8:
    print("Password is too short")
elif password.lower() == password:
    print("Password must contain an uppercase letter")