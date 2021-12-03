#Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters
n=input("enter any word: ")
if n[:3]==n.upper():
    print(n.upper())
else:
    print(n)