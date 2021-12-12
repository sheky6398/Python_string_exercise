# Remove empty strings from a list of strings
# Given:
#
# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# Expected Output:
#
# Original list of sting
# ['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']
#
# After removing empty strings
# ['Emma', 'Jon', 'Kelly', 'Eric']

str = ['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']
result = []
for i in str:
    if i:
        result.append(i)
print(result)