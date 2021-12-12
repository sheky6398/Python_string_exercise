# Reverse a given string
# Given:
#
# str1 = "PYnative"
# Expected Output:
#
# evitanYP

str = input("Enter any word: ")
result = ""
for i in str[::-1]:
    result+=i
print(result)