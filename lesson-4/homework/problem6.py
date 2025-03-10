a = 2
b = 100
s = False
for i in range(a, b):
    for j in range(2, i):
        if i % j == 0:
            s = True
    if s == False:
        print(i)
    else :
        s = False