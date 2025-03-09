a = [1, 43, 54, -34, -23, True, False]
b = len(a)
if b % 2 == 1:
    print(a[b // 2])
else:
    print(a[b // 2 - 1], a[b // 2])