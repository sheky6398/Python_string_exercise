# Write a Python program to remove duplicate words from a given string. Go to the editor
# Sample Output:
# Original String:
# Python Exercises Practice Solution Exercises
# After removing duplicate words from the said string:
# Python Exercises Practice Solution
word = input("Enter any word: ")
word = word.split()
result = ""
for i in word:
    if i not in result:
        result+=i+" "
print(result)