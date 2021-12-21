# A palindrome is a word, phrase, number or other sequence of units that can be read the same way in either direction. Write a function that determines whether the given word or number is a palindrome.

# Examples

#     >>> isPalindrome("Racecar")
#     True
#     >>> isPalindrome(121)
#     True
#     >>> isPalindrome("Never")
#     False
#     >>> isPalindrome("level")
#     True
#     >>> isPalindrome("")
#     False
word = "Never"
word = word.lower()
if word==word[::-1]:
    print(True)
else:
    print(False)


