my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)
    
print("Unsorted: ", my_list)

my_list.sort()
print("Increasing: ", my_list)
my_list.reverse()
print(my_list)