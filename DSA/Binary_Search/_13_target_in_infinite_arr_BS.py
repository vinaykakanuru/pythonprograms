""" Find the position of an element in an infinite sorted array """

from _2_BS_default_template import bs_default_template

## inputs 
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
target = 7


def subset_from_infinte_array(arr, target):
    ## We are finding the subset boundary values of the given infinite array 
    start, end = 0, 1
    while True:
        if arr[end] < target:
            start = end
            end = end * 2
        else:
            break  
    
    return arr, target, start, end

def target_in_infinite_arr_bs(arr, target):
    """ 
    1. Find subset from the infinte array 
    2. Feed the subset to BS template 
    """
    arr, target, start, end = subset_from_infinte_array(arr, target)
    return bs_default_template(arr, target, start, end)


if __name__ == "__main__":
    # output (6)
    print(f"Position of {target} from given Infinite array: ", target_in_infinite_arr_bs(arr, target))

    # output (14)
    print(f"Position of 15 from given Infinite array: ", target_in_infinite_arr_bs(arr, 15))