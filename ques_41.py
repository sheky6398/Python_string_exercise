# Create a new string made of the first, middle, and last characters of each input string
# Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.
#
# Given:
#
# s1 = "America"
# s2 = "Japan"
# Expected Output:
#
# AJrpan

word_1 = "America"
word_2 = "Japan"
print(word_1[0]+word_2[0]+word_1[len(word_1)//2]+word_2[len(word_2)//2]+word_1[-1]+word_2[-1])