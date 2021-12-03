#  Write a Python program to count repeated characters in a string. Go to the editor
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2
n='thequickbrownfoxjumpsoverthelazydog'
dict={}
for i in n:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
for i in dict:
    print(i)