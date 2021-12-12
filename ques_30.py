# Write a Python program to remove duplicate characters of a given string.
word = input("Enter any word: ")
result=""
for i in word:
    if i not in result:
        result+=i
print(result)
#Another Method
b=[]
for i in word:
    if i not in b:
        b.append(i)
print(b)