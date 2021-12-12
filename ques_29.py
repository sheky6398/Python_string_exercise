# Write a Python program to capitalize first and last letters of each word of a given string.
word = input('Enter any word: ')
word = word.split()
# for i in word:
#     print(i[0].upper()+i[1:-1]+i[-1].upper(),end=" ")

#Another Method
# a=[]
# for i in word:
#     a.append(i[0].upper()+i[1:-1]+i[-1].upper())
# print(a)
#Another Method
# a=""
# for i in word:
#     a+=i[0].upper()+i[1:-1]+i[-1].upper()+" "
# print(a)
#Another Method
def first_last(word):
    a = ""
    for i in word:
        a += i[0].upper() + i[1:-1] + i[-1].upper() + " "
    print(a)
result = first_last(word)
print(result)


