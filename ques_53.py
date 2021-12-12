# Replace each special symbol with # in the following string
# Given:
#
# str1 = '/*Jon is @developer & musician!!'
# Expected Output:
#
# ##Jon is #developer # musician##

str = input("Enter any word: ")
result = ""
for i in str:
    if i.isalpha() or i==" ":
        result+=i
    else:
        result+="#"
print(result)