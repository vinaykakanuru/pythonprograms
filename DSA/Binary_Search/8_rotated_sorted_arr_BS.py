rotated_sorted_arr = [11, 12, 15, 18, 2, 5, 6, 8]
target = 15


def binary_search(arr, start, end):
    while(start <= end):
        mid = int(start + (end-start)/2)
        if elem == arr[mid]:
            return mid
        elif elem < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1


def rotate_sorted_arr_bs(arr, target):

    # Apply BS on both sorted arrays 
    # (divide the rotated sorted array from number of times sorted array rotated i.e index of the min number)
    val1 = binary_search(arr1, start, end)
    val2 = binary_search(arr2, start, end)

    return val1, val2


print(rotate_sorted_arr_bs(rotated_sorted_arr, target))