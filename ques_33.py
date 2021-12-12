# Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string.
word = "@W3Resource.Com"
lower_count = 0
upper_count = 0
numeric_count = 0
special_character_count = 0

for i in word:
    if i.islower():
        lower_count+=1
    elif i.isupper():
        upper_count+=1
    elif i.isnumeric():
        numeric_count+=1
    else:
        special_character_count+=1
print("Lowercase",lower_count)
print("Uppercase",upper_count )
print("numeric values",numeric_count)
print("special character",special_character_count)