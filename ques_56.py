# Write the function isReverse(word1, word2) that takes two words as arguments and returns True is the second word is the reverse of the first word.

# Examples

#     >>> isReverse('apple', 'elppa')
#     True
#     >>> isReverse('google', 'apple')
#     False
#     >>> isReverse('google', 'elgoog')
#     True
#     >>> isReverse('apple', 'alppe')
#     False

word1 = input("ENter any number: ")
word2 = input("ENter any number: ")
word_1 = word1[::-1]

if word_1 == word2:
    print(True)
else:
    print(False)
