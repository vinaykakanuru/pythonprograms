""" Find the floor of an element from a sorted array """

arr = [1, 2, 3, 4, 4.6, 10, 10, 12, 19] 
target = 5

def floor_bs(arr, target):
    start, end = 0, len(arr) - 1
    res = -1
    
    while (start <= end):
        mid = int(start + (end - start)//2)
        print(f"start:: {start}, end:: {end}, mid:: {mid}")
        
        # as the same element can be its floor value
        if target == arr[mid]:
            return mid

        if arr[mid] < target:
            res = mid
            start = mid + 1

        if arr[mid] > target:
            end = mid - 1

    return res


# output index of floor of given target (4)
print(f"Floor of {target} from given sorted array: ", floor_bs(arr, target))

# output index of floor of given target (3)
print(f"Floor of 4.5 from given sorted array: ", floor_bs(arr, 4.5))

# output index of ceil of given target (6)
print(f"Floor of 4.5 from given sorted array: ", floor_bs(arr, 10))