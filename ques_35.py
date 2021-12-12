# Write a Python program to remove unwanted characters from a given string. Go to the editor
# Sample Output:
# Original String : Pyth*^on Exercis^es
# After removing unwanted characters:
# Python Exercises
# Original String : A%^!B#*CD
# After removing unwanted characters:
# ABCD
word = input('Enter any word: ')
result=""
for i in word:
    if i.islower():
        result+=i
    elif i.isupper() or i==" ":
        result+=i
print(result)