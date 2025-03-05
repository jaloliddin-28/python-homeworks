a = ["e","u","i","o","a"]
g = input()
text = ""
for i in g.lower():
    if i in a:
        text += "*"
    else:
        text += i
print(text)