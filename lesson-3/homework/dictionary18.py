from collections import defaultdict
a = defaultdict(lambda: 0)
a.update({
    12 : "U",
    13 : "Up",
    14 : "Upd",
    15 : "Upda",
    16 : "Updat",
    17 : "Update",
    18 : "Updat",
    19 : "Upda",
    20 : {"name" : "Jaloliddin", "age" : "19"}
})
print(a[20])  
print(a[21]) 