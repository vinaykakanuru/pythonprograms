l = [64, 34, 25, 12, 22, 11, 90]
sorted_list = sorted(l)

# check the given value with middle index value of the given sorted list
# if val == list[mid] return index(val)
# if val > list[mid] then change min index to mid+1
# else if val < list[mid] decrease nth index to mid-1
# repeat until min_index <= nth index

## Time Complexity
# The time complexity of the binary search algorithm is O(log n). 
# The best-case time complexity would be O(1) when the central index would directly match the desired value. 
# The worst-case scenario could be the values at either extremity of the list or values not in the list.

## Space Complexity
# In the iterative method, the space complexity would be O(1). 
# While in the recursive method, the space complexity would be O(log n). 

# BinarySeacrh with Iteration
def binary_search(list, val):
    idx0 = 0
    idxn = len(list)-1
    
    if idxn < idx0:
        return None

    while idx0 <= idxn:
        mid = (idx0 + idxn) // 2
        if list[mid] == val:
            return f'Found {val} at POS:: {mid}'
        elif val > list[mid]:
            idx0 = mid + 1
        elif val < list[mid]:
            idxn = mid - 1


print('Binary Search with Iteration:', binary_search(sorted_list, 12))

# BinarySeacrh with Recursion
def bsearch(list, idx0, idxn, val):
    if (idxn < idx0):
        return None
    else:
        midval = idx0 + ((idxn - idx0) // 2)

        if val > list[midval]:
            return bsearch(list, midval+1, idxn, val)
        elif val < list[midval]:
            return bsearch(list, idx0, midval-1, val)
        else:
            return f'Found {val} at POS:: {midval}'


print('Binary Search with Recursion:', bsearch(sorted_list, 0, len(sorted_list)-1, 12))
