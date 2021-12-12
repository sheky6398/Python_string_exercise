# Arrange string characters such that lowercase letters should come first
# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.
#
# Given:
#
# str1 = PyNaTive

word = input("Enter any word: ")
result_1 = ""
result_2 = ""
for i in word:
    if i.islower():
        result_1+=i
    else:
        result_2+=i

print(result_1+result_2)