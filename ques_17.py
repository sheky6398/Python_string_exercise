#Write a Python program to sort a string lexicographically.
n=input('Enter any word: ')
print(sorted(n))

#Another method
result = []
for i in sorted(n):
    result.append(i)
print(result)
    