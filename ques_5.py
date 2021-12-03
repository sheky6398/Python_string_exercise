# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

a = input("Enter the word of A: ")
b = input("Enter the word of B: ")
new_a = b[:2]+a[2:]
new_b = a[:2]+b[2:]
print(new_a + " "+ new_b)



#Another method for this question
def swap_string(a,b):
    new_a = b[:2]+a[2:]
    new_b = a[:2]+b[2:]
    return new_a + " "+ new_b
result = swap_string(a,b)
print(result)
