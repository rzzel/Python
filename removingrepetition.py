my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
new = []
# Write your code here.
#
for i in my_list:
    if i not in new:
        new.append(i)
        
print("The list with unique elements only:", new)
print("Original: ", my_list)

