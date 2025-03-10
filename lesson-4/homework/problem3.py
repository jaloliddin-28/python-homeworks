txts = input()
s = 1
txt = txts.lower()
k = []
l = ['a', 'e', 'u', 'i', 'o']
for i in txt:
    k.append(i)
    if s % 3 == 0:
        if i == txt[-1]:
            break
        elif i not in l:
            k.append("_")
            l.append(i)
        elif i in l:
            continue
    s += 1
result = ''.join(k)
print(result)