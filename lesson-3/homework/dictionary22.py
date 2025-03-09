a = {
    12 : "U",
    14 : "Upd",
    13 : "Up",
    15 : "Upda",
    19 : "Upda",
    17 : "Update",
    18 : "Updat",
    16 : "Updat"
}
l = list(a.items())
s = []
for i in l:
    if len(i[1]) <= 4:
        s.append(i)
print(dict(s))