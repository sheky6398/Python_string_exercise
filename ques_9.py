#Write a Python program to remove the characters which have odd index values of a given string.
n=input("Enter any word: ")
print(n[::2])


# Another Method
for i in range(len(n)):
    if i%2==0:
        print(n[i],end="")


#Another Method 
for i in range(len(n)):
    result = ""
    if i%2==0:
        print(result + n[i],end="")


#ANother Method
def even(n):
    result = ""
    for i in range(len(n)):
        if i%2==0:
            result = result + n[i]
    return result
result = even(n)
print(result)