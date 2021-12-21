# Write the function startWithVowel(word) that takes in a word as argument and returns a substring that starts with the first vowel found in the word. The function returns 'No vowel' if the word does not contain vowel.

# Examples

#     >>> startWithVowel('apple')
#     'apple'
#     >>> startWithVowel('google')
#     'oogle'
#     >>> startWithVowel('xyz')
#     'No vowel'

vowel = ('a','e','i','o','u')
word = 'xyz'
if word.startswith(vowel):
    print(word)
elif not word.startswith(vowel):
    print(word[1:])
else:
    print("No vowel")