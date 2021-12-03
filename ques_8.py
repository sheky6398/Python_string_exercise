#Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
n = input("Enter any word: ")
print(n[-1]+n[1:-1]+n[0])

# Another Method
def exchanged(n):
    return n[-1]+n[1:-1]+n[0]
result = exchanged(n)
print(result)