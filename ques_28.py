# Write a Python program to find the maximum occurring character in a given string.
word = input("Enter any word: ")
dict = {}
for i in word:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
for i,j in sorted(dict.items(),key=lambda x:x[1],reverse=True)[:1]:
    print(i)