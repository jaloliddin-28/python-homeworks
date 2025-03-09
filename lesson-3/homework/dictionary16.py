a = {
    12 : "U",
    13 : "Up",
    14 : "Upd",
    15 : "Upda",
    16 : "Updat",
    17 : "Update",
    18 : "Updat",
    19 : "Upda",
    20 : {"name" : "Jaloliddin", "age" : "19"}
}
c = False
for i in a:
    if isinstance(a[i], dict):
        c = True
        break
print(c)