a = (2, 45, -4, -5, 2, 56, 35, 643, 2, 53, 2, -34)
m = []
for i in a:
    if m.count(i) == 0:
        m.append(i)
print(tuple(m))