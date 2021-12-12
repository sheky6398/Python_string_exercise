#  Write a program to count occurrences of all characters within a string
# Given:
#
# str1 = "Apple"
# Expected Outcome:
#
# {'A': 1, 'p': 2, 'l': 1, 'e': 1}

word = input("Enter any word: ")
dict={}
for i in word:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)