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
b = dict(sorted(a.items(), key = lambda item: item[1]))
print(b)