a = [1, 2, 3, 5, 7, 8, 3, 2]
b = [1, 6, 5, 4, 7, 9]
l = []
for i in a:
    if b.count(i) == 0:
        l.append(i)
for j in b:
    if a.count(j) == 0:
        l.append(j)
print(l)