main_list = []
other_chars = [',', '!', '.', '?', '\'', "\"", '@', '\n', '#', '%', "*", "(", ")"]
with open(r"C:\Users\user\Desktop\MAAB\python-homeworks\lesson-6\homework\sample.txt", mode = 'r') as file:
    txt = file.read()
    txt = txt.lower()
for i in other_chars:
    if i == '\n':
        txt = txt.replace(i, ' ')
    else :
        txt = txt.replace(i, '')
main_list = txt.split(' ')
main_dict = {}
keys = list(main_dict.keys())
for j in main_list:
    if j not in other_chars and j not in keys and j != '':
        main_dict.update({j : main_list.count(j)})
main_dict = dict(sorted(main_dict.items(), key = lambda item: item[1], reverse = True))
print("Total words: ", len(main_list))
print("Top 5 most common words:")
for i in range(5):
    print(f"{list(main_dict.keys())[i]} - {main_dict[list(main_dict.keys())[i]]} times")
with open(r"C:\Users\user\Desktop\MAAB\python-homeworks\lesson-6\homework\word_counter_txt.txt","w") as f:
    f.write("Word Count Report\n")
    f.write(f"Total Words: {len(main_list)}\nTop 5 Words:\n")
    for i in range(5):
        f.write(f"{list(main_dict.keys())[i]} - {main_dict[list(main_dict.keys())[i]]} times\n")