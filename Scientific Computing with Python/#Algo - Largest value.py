#Algo - Largest value


large_num = None
the_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]


print( "Largest value:", large_num)


for value_i in the_array:
    
    print("Current Largest number:",  large_num, "\nNew value to compare:", value_i)
    
    if large_num == None:
        large_num = value_i

    elif large_num< value_i:
        large_num = value_i

    print ("New Largest value:", large_num)


print("The Largest number in the array is:", large_num)