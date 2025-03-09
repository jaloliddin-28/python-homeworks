a = [1, 45, 56, 3, 4, 7, 8, 3, 1, 56, 45, -5, 43, 1, 3]
b = []
for i in a:
    if b.count(i) == 0:
        b.append(i) 
print(b)