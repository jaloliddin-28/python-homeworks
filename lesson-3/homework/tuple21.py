a = (2, 45, -4, -5, 2, 56, 35, 643, 2, 53, 2, -34)
b = int(input("Enter the number: "))
c = []
for i in a:
    for j in range(b):
        c.append(i)
print(tuple(c))