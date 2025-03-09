l = [1, 2, -4, 2, 23, 1, 78, -4, -56, 23, 0, -5]
m = []
for i in l:
    if m.count(i) == 0:
        m.append(i)
print(m)