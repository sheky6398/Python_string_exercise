# Write a Python code to remove all characters except a specified character in a given string. Go to the editor
# Original string
# Python Exercises
# Remove all characters except P in the said string:
# P
# Original string
# google
# Remove all characters except g in the said string:
# gg
# Original string
# exercises
# Remove all characters except e in the said string:
# eee
word = input("Enter any word: ")
res = input("Choose any word: ")
a=""
for i in word:
    if i==res:
        a+=i
print(a)

