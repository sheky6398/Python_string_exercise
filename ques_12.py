# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically). Go to the editor
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red
n = 'red, white, black, red, green, black'
n = n.split(',')
result=""
for i in sorted(n):
    if i not in result:
        result+=i
print(result)


# Another method
def unique(n):
    result=""
    for i in sorted(n):
        if i not in result:
            result+=i
    return result
new = unique(n)
print(new)

