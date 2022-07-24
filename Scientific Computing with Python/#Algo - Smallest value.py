#Algo - Smallest value


small_num = None
the_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]


print( "Smallest value:", small_num)


for value_i in the_array:
    
    print("Current smallest number:",  small_num, "\nNew value to compare:", value_i)
    
    if small_num == None:
        small_num = value_i

    elif value_i < small_num:
        small_num = value_i

    print ("New smallest value:", small_num)


print("The smallest number in the array is:", small_num)