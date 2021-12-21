# Write a function mirrorText(word1, word2) that takes in 2 words as arguments and returns a new word in the following order: word1word2word2word1.

# Examples

#     >>> mirrorText('hello','world')
#     'helloworldworldhello'
#     >>> mirrorText('apple','orange')
#     'appleorangeorangeapple'
#     >>> mirrorText('google','yahoo')
#     'googleyahooyahoogoogle'

a= 'apple'
b = 'orange'
print(a+b+b+a)
