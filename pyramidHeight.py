blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#	
layer = 1 
height = 0

while layer <= blocks:

    height += 1
    blocks -= layer
    layer +=1

print("The height of the pyramid:", height)

