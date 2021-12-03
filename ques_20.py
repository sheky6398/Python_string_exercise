#Write a Python program to reverse a string.
n=input("Enter any word: ")
print(n[::-1])


#Another method

for i in range(len(n)-1,-1,-1):
    print(n[i],end="")