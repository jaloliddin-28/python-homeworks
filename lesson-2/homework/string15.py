a = input("Enter a sentence: ")
text = a.split()
acronym = ""
for word in text:
    acronym += word[0]
print(acronym)