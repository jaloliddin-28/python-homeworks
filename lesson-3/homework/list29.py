l = [12, 43, 3, 7, 8, 10, 16, 44, 55]
n = int(input("Index: "))
if n < len(l):
    l.remove(l[n])
    print(l)
else:
    print("Index out of range. ")