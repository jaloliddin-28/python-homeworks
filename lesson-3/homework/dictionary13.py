a = {
    12 : "U",
    13 : "Up",
    14 : "Upd",
    15 : "Upda",
    16 : "Updat",
    17 : "Update",
    18 : "Updat",
    19 : "Upda",
    20 : "Upd"
}
b = {}
l = list(a.keys())
m = list(a.values())
for i in range(len(a)):
    b.update({m[i] : l[i]})
print(b)