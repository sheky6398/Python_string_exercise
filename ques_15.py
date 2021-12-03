#Write a Python function to reverses a string if it's length is a multiple of 4.
n=input("Enter any word: ")
if len(n)%4==0:
    print(n[::-1])
else:
    print(n)