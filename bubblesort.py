my_list = [] #empty list
swapped = True 
num = int(input("how many: ")) #numbers to be sorted

for i in range(num):
    val = float(input("Enter list number: " ))
    my_list.append(val) #put the input into the list
    
print("Unsorted: ",my_list)
    
while swapped:
    swapped = False #this is no swapped
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i +1]:
            swapped = True #with swapped
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i] #exhanging position
        
print("Sorted: \n" , my_list)