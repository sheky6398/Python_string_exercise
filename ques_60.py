# Write a function echoWord(word) that takes in a word as arguments and returns a word that repeats itself based on the number of letter in the word.

# Examples

#   >>> echoWord('hi') 
#   'hihi'
#   >>> echoWord('apple')
#   'appleappleappleappleapple'
#   >>> echoWord('ice')
#   'iceiceice'
word = 'apple'
count=0
for i in word:
    count+=1
print(word*count)
