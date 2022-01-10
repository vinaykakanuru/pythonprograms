""" Find the index of first element from infinite Binary sorted array """

from _5_first_last_occurence_sorted_arr_BS import first_occurence_sorted_arr
from _13_target_in_infinite_arr_BS import subset_from_infinte_array

## inputs
arr = [0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
target = 1

def first_idx_binary_infinte_arr_bs(arr, target):
    """ 
    1. Find the subset from given infinite binary sorted array
    2. Feed the subset to first_occurence template of BS
    """
    arr, target, start, end = subset_from_infinte_array(arr, target)
    return first_occurence_sorted_arr(arr, target)


# output index of first occurence of 1 in given binary infinite sorted array (9)
print(f"Fisrt occurence of {target} from given Biary Infinite array: ", first_idx_binary_infinte_arr_bs(arr, target))