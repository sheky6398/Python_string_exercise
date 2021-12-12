# Create a mixed String using the following rules
# Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.
# Given:
#
# s1 = "Abc"
# s2 = "Xyz"
# Expected Output:
#
# AzbycX


word_1 = input("Enter first word: ")
word_2 = input("Enter second word: ")
print(word_1[0]+word_2[-1])
