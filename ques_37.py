# Write a Python program to extract numbers from a given string. Go to the editor
# Sample Output:
# Original string: red 12 black 45 green
# Extract numbers from the said string: [12, 45]
word = input("Enter any word: ")

result = []
for i in word.split():
    if i.isnumeric():
        result.append(int(i))
print(result)

#Another Method

print([int(i) for i in word.split() if i.isnumeric()])
