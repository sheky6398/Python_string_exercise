# Calculate the sum and average of the digits present in a string
#
# Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.
#
# Given:
#
# str1 = "PYnative29@#8496"
# Expected Outcome:
#
# Sum is: 38 Average is  6.333333333333333

word = input('Enter any word: ')
result = ""
sum=0
for i in word:
    if i.isdigit():
        result+=i
for i in result:
    sum+=int(i)
print(f'Sum is {sum} Average is {sum/len(result)}')