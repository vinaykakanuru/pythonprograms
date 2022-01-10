""" Find the target element from the rotated sorted array """

from _7_times_array_rotated import num_of_times_rotated

## input values
rotated_sorted_arr = [11, 12, 15, 18, 2, 5, 6, 8]
target = 15


def binary_search(arr, target, start, end):
    """ A normal BS template helps to find the target element in given sorted arr 
    Returns index of the target if present else -1
    """
    while(start <= end):
        mid = int(start + (end-start)/2)
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def rotate_sorted_arr_bs(arr, target):
    """ Solution to find the index of given target from rotated sorted array 
    1. Find the index of min element from rotated sorted array
    2. Divide the given rotated sorted array into two parts 
    3. Feed the arrays to BS template to find the target element, Target presents in only one part of the arr.
    4. If target is not present in both parts we consider the traget element is not present in given rotated sorted arr. 
    """
    start, end = 0, len(arr) - 1

    ## Divide the rotated sorted array from number of times sorted array is rotated i.e index of the min number
    ## And pass the (start, end) range based on min_idx found
    min_idx = num_of_times_rotated(arr)
    arr1, arr2 = arr[:min_idx], arr[min_idx:]
    print(f"Array1: {arr1}, Array2: {arr2}")
    
    ## Apply BS on both sorted arrays 
    ## You can find it in either of the arr or target is not present in the main arr.
    val1 = binary_search(arr, target, start, min_idx - 1)
    val2 = binary_search(arr, target, min_idx, end)
    
    if val1 == -1 and val2 == -1:
        return -1
    
    return val2 if val1 < 0 else val1 

## outputs index of the target from the rotated sorted array (2)
print(rotate_sorted_arr_bs(rotated_sorted_arr, target))