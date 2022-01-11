""" Search an element from Bitonic array """

from _2_BS_default_template import bs_default_template
from _3_desc_order_BS import sorted_array_desc
from _17_peak_element_BS import peak_element

## inputs 
arr = [1, 3, 8, 12, 4, 2]
target = 4


def search_in_bitonic_arr_bs(arr, target):
    """
    1. Find peak idx from given Bitonic array
    2. Divide the given array boundaries using peak idx
    3. Feed both Asc and Desc array bounds to BS templates to look for the target
    """
    peak_idx = peak_element(arr)
    val1 = bs_default_template(arr, target, start=0, end=peak_idx-1)
    val2 = sorted_array_desc(arr, target, peak_idx, end = len(arr) - 1)

    if val1 == -1 and val2 == -1:
        return -1
    
    return val2 if val1 < 0 else val1 


if __name__ == "__main__":
    print(search_in_bitonic_arr_bs(arr, target)) # outputs (4)
    print(search_in_bitonic_arr_bs(arr, 8)) # outputs (2)
