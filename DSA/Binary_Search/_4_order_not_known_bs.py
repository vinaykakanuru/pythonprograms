""" order not known (how to find the given array is sorted in Asc/Desc order) """

from _2_BS_default_template import bs_default_template
from _3_desc_order_BS import sorted_array_desc

## inputs
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr = [20, 17, 15, 14, 13, 12, 10, 9, 8, 4]
target = 10


def order_not_known_bs(arr, target):
    if len(arr) <= 1:
        return "Not a valid array for BS"

    else:
        ## edge case: 
        # if starting elements are duplicates, go until we find some difference between two adjacent elements
        elem_1, elem_2 = 0, 0
        i, n = 0, len(arr) - 1
        while (i < n):
            if arr[i] != arr[i+1]:
                elem_1, elem_2 = arr[i], arr[i+1]
                break
            i += 1

        ## actual BS starts here
        if elem_1 < elem_2:
            return bs_default_template(arr, target) ## returns (9)
        
        if elem_1 > elem_2:
            return sorted_array_desc(arr, target) ## returns (6)
        

if __name__ == "__main__":
    print(order_not_known_bs(arr, target)) 