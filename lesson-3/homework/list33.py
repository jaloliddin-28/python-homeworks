l = [1, 2, 43, 54, 2, 65, 78, -4, 2, -3, 2, -5]
element = 2
for i in l:
    if i == element:
        print(l.index(i), end = " ")
        l.remove(element)    