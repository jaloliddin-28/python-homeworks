l = [12, 43, 3, 7, 8, 10, 16, 44, 55]
starts = int(input("Beginning index: "))
ends = int(input("Ending index: "))
if ends < len(l):
    print(min(l[starts : (ends + 1)]))
else: 
    print("Out of range.")