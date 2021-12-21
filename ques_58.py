# Write the function capitalizeVowels(word) that returns the word with all the vowels capitalized.

# Examples

#     >>> capitalizeVowels('apple')
#     'ApplE'
#     >>> capitalizeVowels('google')
#     'gOOglE'
def capitalizeVowels(word):
    result = ""
    vowels = ('a', 'e', 'i', 'o', 'u') 
    for i in "google":
        if i not in vowels:
            result+=i
        else:
            result+=i.upper()
    return result
print(capitalizeVowels('google'))