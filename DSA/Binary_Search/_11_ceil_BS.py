""" Find the ceil of an element from a sorted array """

arr = [1, 2, 3, 4, 8, 10, 10, 12, 19] 
target = 5

def ceil_bs(arr, target):
    start, end = 0, len(arr) - 1
    res = -1
    
    res = -1
    while (start <= end):
        mid = int(start + (end - start)/2) 
        print(f"start:: {start}, end:: {end}, mid:: {mid}")
        
        # as the same element can be its Ceil value
        if arr[mid] == target: 
            return mid

        if arr[mid] > target:
            res = mid
            end = mid - 1

        if arr[mid] < target:
            start = mid + 1

    return res


# output index of ceil of given target (4)
print(f"Ceil of {target} from given sorted array: ", ceil_bs(arr, target))

# output index of ceil of given target (5)
print(f"Ceil of {target} from given sorted array: ", ceil_bs(arr, 8.1))

# output index of ceil of given target (6)
print(f"Ceil of {target} from given sorted array: ", ceil_bs(arr, 10))