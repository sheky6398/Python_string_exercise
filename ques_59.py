# Write the function startEndVowels(word) that returns True if the word starts and ends with vowels.

# Examples

#     >>> startEndVowels('apple')
#     True
#     >>> startEndVowels('google')
#     False
#     >>> startEndVowels('A')
#     True
#     >>> startEndVowels('')
#     False

def startEndVowels(word):
    vowels = ('a', 'e', 'i', 'o', 'u','A','E','I','O','U')
    if word.startswith(vowels):
        print(True)
    else:
        print(False) 
startEndVowels('apple')