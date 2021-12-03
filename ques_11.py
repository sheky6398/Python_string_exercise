#Write a Python script that takes input from the user and displays that input back in upper and lower cases.
n=input("Enter any word: ")
print(n.lower())
print(n.upper())


# Another method
def lower_upper(n):
    return n.lower(),n.upper()
result = lower_upper(n)
print(result)