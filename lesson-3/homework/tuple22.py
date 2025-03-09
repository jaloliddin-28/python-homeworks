a = int(input("Starting number: "))
b = int(input("Ending number: "))
c = []
for i in range(a, b+1):
    c.append(i)
print(tuple(c))