l = [64, 34, 25, 12, 22, 11, 90]

# It is also called as a sequential search, Seaching the given element iterating thorugh each element in the given list.
# Every element is checked and if a match is found then that particular item is returned,
# otherwise the search continues till the end of the data structure.

## Time Complexity
# It is named as linear because its time complexity is of the order of n, BigO notation is O(n).

## Space Complexity
# BigO Notation is O(1) because we are perfoming search operation on one element only in each iteration.

def linear_search(list, val):
    search_at = 0
    search_res = False
    # Match the value with each data element
    while search_at < len(list) and search_res is False:
        # with help of search_res is False cond we reduce time complexity by ignoring searching rest of elements
        if list[search_at] == val:
            search_res = True
        else:
            search_at = search_at + 1
    return 'Found ' + str(val) + ' at POS: ' + str(search_at)


print(linear_search(l, 34))
