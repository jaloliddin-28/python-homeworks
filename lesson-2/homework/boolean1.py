a = input("Username: ")
b = input("Password: ")
if bool(a) and bool(b):
    print("None is empty")
elif bool(a) or bool(b):
    print("One is empty")
else :
    print("Both are empty")