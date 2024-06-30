# Create an Array in Python

import array as arr
new_arr = arr.array('i',[1,2,3,4,5])
print("The new array is : ",end = ' ')
for i in range (0,5):
    print(new_arr[i],end=' ')

print("\n")
    
another_arr = arr.array('d',[1.5,2.5,5.0,6.8,8.9])
print("The float array is : ",end = ' ')
for i in range(0,4):
    print(another_arr[i],end= ' ')