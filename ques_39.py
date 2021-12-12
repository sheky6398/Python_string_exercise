# Write a program to create a new string made of an input string’s first, middle, and last character.
#
# Given:
#
# str1 = "James"
# Expected Output:
#
# Jms
word = input("Enter any word: ")
print(word[0]+word[len(word)//2]+word[-1])