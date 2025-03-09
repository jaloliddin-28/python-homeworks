a = (2, 45, -4, -5, 2, 56, 35, 643, 2, 53, 2, -34)
c = int(input("Enter the size of the subtuple."))
d = []
for i in range(0, len(a), c):
    d.append(a[i : i + c])
print(tuple(d))