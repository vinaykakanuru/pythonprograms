## finding the second largest from the given array
sort_arr = [10, 20, 4, 45, 99, 99]
rem_max_arr = [10, 20, 4, 45, 99, 99]
range_arr = [10, 20, 4, 45, 99, 99]
arr = [10, 20, 4, 45, 99, 99]

## method - 1 (Sort)
def find_large_using_sort(arr):
    """ 
    It fails if arr has two equal max integer 
    But can be handled with help of set (removing duplicates)
    """
    arr = list(set(arr))
    arr.sort()
    return arr[-2]


## method - 2 (Remove max and find the max)
def find_largest_remove_max(arr):
    """ 
    It fails if arr has two equal max integer 
    But can be handled with help of set (removing duplicates)
    """
    arr = list(set(arr))
    arr.remove(max(arr))
    return max(arr)


## method - 3 and method - 4 are same 
# but here we are traversing from index-2
def find_largest_range(arr):
    mx = max(arr[0], arr[1])
    second_max = min(arr[0], arr[1])
    n = len(arr)
    
    # swapping largest, second_largest while traversing the arr
    for i in range(2, n):
        if arr[i] > mx:
            second_max = mx
            mx = arr[i]
        elif arr[i] > second_max and arr[i] != mx:
            second_max = arr[i]
 
    return second_max


## method - 4 Traversing whole array and swapping largest and second_largest
def find_largest(arr):
    if len(arr) < 2:
        return "Array should contain atleast two elements"

    largest = arr[0]
    second_largest = arr[0]
    
    # swapping largest, second_largest while traversing the arr
    for i in range(len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
 
    return second_largest
 

print(find_large_using_sort(sort_arr))
print(find_largest_remove_max(rem_max_arr))
print(find_largest_range(range_arr))
print(find_largest(arr))