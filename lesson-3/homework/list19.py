a = [1, 43, 54, -34, -23, True, False, "Painter"]
b = -23
c = a.index(b)
a.remove(b)
a.insert(c, False)
print(a)