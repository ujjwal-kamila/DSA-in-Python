# Let's create an array and apply all array methods
'''
append
Count 
extend
fromlist
index
insert 
pop 
remove
reverse 
to list
'''

# Create an initial array
array = ['A', 'E', 'I', 'O']

# Append 'U' to the array
array.append('U')
print("After append 'U', the updated array is:", array)

# Count occurrences of 'A' in the array
count_A = array.count('A')
print("Count of 'A' in the array:", count_A)

# Extend the array with 'C'
array.extend(['C'])
print("After extend 'C', the updated array is:", array)

# Get the index of 'E'
get_index = array.index('E')
print("The index of 'E' is:", get_index)

# Insert 'Z' at index 2
array.insert(2, 'Z')
print("Array after inserting 'Z':", array)

# Pop the last element
pop_element = array.pop()
print("Array after popping the last element:", array)
print("Popped element is:", pop_element)

# Remove the first occurrence of 'Z'
array.remove('Z')
print("Array after removing 'Z':", array)

# Reverse the entire array
array.reverse()
print("Reversed array is:", array)
