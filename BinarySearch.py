l = [64, 34, 25, 12, 22, 11, 90]
sorted_list = sorted(l)

# check the given val with mid index value of given sorted list
# if val == list[mid] return index(val)
# if val > list[mid] then increase min index with mid+1
# else decrease nth index to mid-1
# repeat until min_index <= nth index


def binary_search(list, val):
    idx0 = 0
    idxn = len(list)-1

    while idx0 <= idxn:
        mid = (idx0 + idxn) // 2
        if list[mid] == val:
            return 'Found ' + str(val) + ' at POS: ' + str(mid)
        elif val > list[mid]:
            idx0 = mid + 1
        elif val < list[mid]:
            idxn = mid - 1

    if idxn < idx0:
        return None


print('Binary Search: ', binary_search(sorted_list, 12))

# BinarySeacrh with Recursion
def bsearch(list, idx0, idxn, val):
    if (idxn < idx0):
        return None
    else:
        midval = idx0 + ((idxn - idx0) // 2)

        if list[midval] > val:
            return bsearch(list, idx0, midval-1, val)
        elif list[midval] < val:
            return bsearch(list, midval+1, idxn, val)
        else:
            return 'Found ' + str(val) + ' at POS: ' + str(midval)


print('Binary Search with recursion: ', bsearch(sorted_list, 0, len(sorted_list)-1, 12))
