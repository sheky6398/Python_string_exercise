# Write the function removeVowels(word) that removes all the vowels ('a', 'e', 'i', 'o', 'u') in a word and returns the remaining letters in the word.

# Examples

#     >>> removeVowels('apple')
#     "ppl"
#     >>> removeVowels('Apple')
#     "ppl"
#     >>> removeVowels('Banana')
#     'Bnn'



result = ""
vowels = ('a', 'e', 'i', 'o', 'u') 
for i in "Banana":
    if i not in vowels:
        result+=i
print(result)