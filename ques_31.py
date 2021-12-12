# Write a Python program to compute sum of digits of a given string.
a=input("Enter any word: ")
b=""
sum=0
for i in a:
    if i.isnumeric():
        b+=i
for i in b:
    sum+=int(i)
print(f"Sum of {b} is ",sum)