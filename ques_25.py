# Write a Python program to lowercase first n characters in a string.
str = input("Enter any word: ")
n = int(input("Enter the number: "))
print(str[:n].lower()+str[n:].upper())
