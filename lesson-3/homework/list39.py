l = [1, 2, -43, 54, 23, 65, 78, -4, -56, -3, 0, -5]
m = int(input("How many elements in a sublist?"))
a = []
for i in range(0, len(l), m):
    a.append(l[i:i + m])
print(a)