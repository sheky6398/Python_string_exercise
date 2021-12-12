# Write a Python program to count and display the vowels of a given text.
word = input("Enter any word: ")
vowel = "aeiouAEIOU"
count = 0
for i in word:
    if i in vowel:
        count+=1
print(f"Total vowel letter in {word} is: ",count)
# Another method
vowel = ['a','e','i','o','u']
count=0
print(len([i for i in word if i in vowel]))
print([i for i in word if i in vowel])