""" Count of an element in a given sorted array """
from _5_last_occurence_sorted_arr_BS import first_occurence_sorted_arr, last_occurence_sorted_arr

## inputs
arr = [2, 4, 10, 10, 10, 18, 20]
target = 10


def count_elem_sorted_arr(arr, target):
    """ If element repeats in sorted arr that means all same elements sits together 
    1. Find first_occurence of the target from sorted array
    2. Find last_occurence of the target from sorted array
    3. Find [last_occurence - first_occurence + 1]
    """
    first_occurence = first_occurence_sorted_arr(arr, target)
    last_occurence = last_occurence_sorted_arr(arr, target)

    return last_occurence - first_occurence + 1

## outputs (3)
print(count_elem_sorted_arr(arr, target))