l = [64, 34, 25, 12, 22, 11, 90]
sorted_list = sorted(l)

# check the given val with mid index value of given sorted list
# if val == list[mid] return index(val)
# if val > list[mid] then increase min index with mid+1
# else decrease nth index to mid-1
# repeat until min_index <= nth index

# Time and Space complexity
# The time complexity of the binary search algorithm is O(log n). 
# The best-case time complexity would be O(1) when the central index would directly match the desired value. 
# The worst-case scenario could be the values at either extremity of the list or values not in the list.


def binary_search(list, val):
    idx0 = 0
    idxn = len(list)-1

    while idx0 <= idxn:
        mid = (idx0 + idxn) // 2
        if list[mid] == val:
            return f'Found {val} at POS:: {mid}'
        elif val > list[mid]:
            idx0 = mid + 1
        elif val < list[mid]:
            idxn = mid - 1

    if idxn < idx0:
        return None


print('Binary Search:', binary_search(sorted_list, 12))

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


print('Binary Search with recursion:', bsearch(sorted_list, 0, len(sorted_list)-1, 12))
