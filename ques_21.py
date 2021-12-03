#Write a Python program to reverse words in a string
n=input("Enter any word: ")
n=n.split()
print(n[::-1])


#Another method
for i in n[::-1]:
    print(i,end=" ")