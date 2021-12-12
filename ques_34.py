# Write a Python program to swap cases of a given string. Go to the editor
# Sample Output:
# pYTHON eXERCISES
# jAVA
# nUMpY
word = input('Enter any word: ')
result = ""
for i in word:
    if i.islower():
        result+=i.upper()
    else:
        result+=i.lower()
print(result)
