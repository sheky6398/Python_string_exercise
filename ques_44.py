# Find all occurrences of a substring in a given string by ignoring the case
# Write a program to find all occurrences of “USA” in a given string ignoring the case.
#
# Given:
#
# str1 = "Welcome to USA. usa awesome, isn't it?"
# Expected Outcome:
#
# The USA count is: 2

str1 = "Welcome to USA. usa awesome, isn't it?"
str2 = str1.lower()
print(str2.count("usa"))
