# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. Go to the editor
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String
n = input("Enter any word: ")
if len(n)>=2:
    print(n[:2]+n[-2:])
else:
    print("Empty String")

#Another method by using Fucntion
def string(n):
    if len(n)>=2:
        return n[:2]+n[-2:]
    else:
        return "Empty String"
result = string(n)
print(result)