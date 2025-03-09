a = [12, 13, 14, 15, 16]
b = ["Hello", "Life", "Enjoy", "Study", "Pray"]
c = {}
for i in range(min(len(a), len(b))):
    c.update({a[i] : b[i]})
print(c)