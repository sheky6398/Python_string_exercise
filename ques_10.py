#Write a Python program to count the occurrences of each word in a given sentence.
# n = 'the quick brown fox jumps over the lazy dog.'
n=input("Enter any sentence: ")
n = n.split()
dict = {}
for i in n:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)



# Another Method
def search(n):
    dict={}
    for i in n:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    return dict
result = search(n)
print(result)