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
d = False
b ={
    12 : "Al",
    13 : "Hello",
    18 : "Need"
}
l = list(a.keys())
for i in b:
    if l.count(i) != 0:
        d = True
        break
print(d)