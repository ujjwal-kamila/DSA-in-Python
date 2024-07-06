# Assignment-1: Array and List

# 1. Given an array with some integer type values, write a Python script to sort array values
def sort_array(arr):
    return sorted(arr)

# Example usage
array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_array = sort_array(array)
print("Sorted array:", sorted_array)





# 2. Given a list of heterogeneous elements, write a Python script to remove all the non-integer values from the list.
def remove_non_integers(lst):
    return [x for x in lst if isinstance(x, int)]

# Example usage
heterogeneous_list = [1, 'a', 3.14, 2, 'b', 4, 5.67, True, 6]
filtered_list = remove_non_integers(heterogeneous_list)
print("Filtered list:", filtered_list)



# 3. Write a Python script to calculate the average of elements of a list.




# 4. Write a Python script to create a list of the first N prime numbers.



# 5. Write a Python script to create a list of the first N terms of a Fibonacci series.

