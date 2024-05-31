# How to create a array in python

#using array modules

import array as arr
my_array = arr.array('i',[1,3,2,4,5,6,8,7])
print(type(my_array))
print(my_array)

# printing array elements using loop
print("Array elements")
for i in my_array :
    print(i,end=' ')

print("\n")

# using while loops
i = 0 
while (i < len(my_array)):
    print(my_array[i])
    i +=1
    

# using  numpy 
import numpy as np

# Creating a numpy array
my_array = np.array([1, 2, 3, 4, 5])
print(type(my_array))  
print(my_array)  