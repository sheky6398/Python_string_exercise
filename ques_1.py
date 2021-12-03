#Write a Python program to calculate the length of a string.
n=input("Enter any word: ")
print(f"Length of {n} is {len(n)}")

#Another method for calculate length of any word
count=0
for i in n:
    count+=1
print(count)