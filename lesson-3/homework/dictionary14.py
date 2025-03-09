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
b = "Upd"
l = []
for i in a:
    if a.get(i) == b:
        l.append(i)
print(l)