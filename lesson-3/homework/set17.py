a = {2, 4, 7, -32, -23, 45, 5, 3}
b = set()
for i in a:
    if i % 2 == 1:
        b.add(i)
print(b)