text = input("Enter a string: ")

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
for i in text:
    if i.isalpha(): 
        if i in vowels:  
            vowel_count += 1
        else:  
            consonant_count += 1
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")