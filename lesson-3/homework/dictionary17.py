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
b = 20
c = "name"

if b in a:
    g = a[b]
    if isinstance(g, dict):
        if c in g:
            print(g[c])