# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. Go to the editor
# Sample String : 'restart'
# Expected Result : 'resta$t'
a=input("Enter any word: ")
res_1 = a[0]
a = a.replace(a[0],'$')
print(res_1+a[1:])



#Another method by using Function
def change_char(a):
    char = a[0]
    a = a.replace(a[0],'$')
    return char + a[1:]
result = change_char(a)
print(result)