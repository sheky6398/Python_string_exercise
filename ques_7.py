#Write a Python program to remove the nth index character from a nonempty string.
word = input("Enter any word: ")
n=int(input("Enter the nth index: "))
print(word[:n]+word[n+1:])

#Another Method 
def index(word,n):
    return word[:n]+word[n+1:]
result = index(word,n)
print(result)