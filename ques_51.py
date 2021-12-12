#  Removal all characters from a string except integers
# Given:
#
# str1 = 'I am 25 years and 10 months old'
# Expected Output:
#
# 2510

str = input("Enter any word: ")
result = ""
for i in str:
    if i.isdigit():
        result+=i
print(result)