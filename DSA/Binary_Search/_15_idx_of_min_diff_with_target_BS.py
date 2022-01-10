""" Find the index of an element from sorted array which gives min difference with the given target. """

# Inputs
arr = [1, 3, 8, 10, 12, 15]
target = 12

def idx_of_min_diff_with_target(arr, target):
    """ 
    1. Apply normal BS template if target present that is our value
    2. Else find the min of abs difference with ended up (start, end) neighnors of our target
    """
    start, end = 0, len(arr) - 1
    while (start <= end):
        mid = int(start + (end - start)//2)

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    min_start, min_end = abs(arr[start] - target), abs(arr[end] - target)

    return start if min_start < min_end else end


# output index (4)
print(f"Position of min element with which our {target} gives min absolute difference: ", idx_of_min_diff_with_target(arr, target))

# output index (2)
print(f"Position of min element with which our 9 gives min absolute difference: ", idx_of_min_diff_with_target(arr, 9))