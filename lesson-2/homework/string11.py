a = input("Enter a string: ")
if any(i.isdigit() for i in a):
    print("The string contains digits.")
else:
    print("The string does not contain any digits.")