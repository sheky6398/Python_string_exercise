# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. Go to the editor
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'
n = input("Enter any word: ")
if len(n)>=3:
    if n.endswith('ing'):
        print(n.replace('ing','ly'))
    else:
        print(n+'ing')
else:
    print(n)


    
# Another method
def string(n):
    if len(n)>=3:
        if n.endswith('ing'):
            return n.replace('ing','ly')
        else:
            return n+'ing'
    else:
        return n
result = string(n)
print(result)


