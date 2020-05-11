l = [64, 34, 25, 12, 22, 11, 90]

# In this type of search, a sequential search is made over all items one by one.
# Every item is checked and if a match is found then that particular item is returned,
# otherwise the search continues till the end of the data structure.

def LinearSearch(list, val):
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

print(LinearSearch(l, 34))