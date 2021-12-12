# Find words with both alphabets and numbers
# Write a program to find words with both alphabets and numbers from an input string.
# Given:
#
# str1 = "Emma25 is Data scientist50 and AI Expert"
# Expected
# Output:
#
# Emma25
# scientist50

str = input("Enter any word: ")
result = ""
for i in str.split():
    if not i.isalpha():
        print(i)
