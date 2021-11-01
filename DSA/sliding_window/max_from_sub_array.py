## from given window size of sub_arrays find the maximum number from the provided array

## Input:: arr = [1, 3, -1, -3, 5, 3, 6, 7] and k = 3
## Output:: Array of [len(arr) - k + 1] elements

## Test case 1
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3 
output = [3, 3, 5, 5, 6, 7]

## Test case 2
arr = [1, 24, 7, 9, 1, 8, 2, 65, 8, 9, 3, 6]
# k = 3  ==> output = [24, 24, 9, 9, 8, 65, 65, 65, 9, 9]
k = 5
output = [24, 24, 9, 65, 65, 65, 65, 65]


def max_from_sub_array(arr, k):
    i, j = 0, 0
    # bit confusing how elements are playing here in this list
    # treat this helper list as a queue and we are removing the first elements which are less than arr[j]
    # and keeping other numbers (even though smaller than arr[j]) after arr[j] in helper_list
    help_list = [] 
    res = []

    while j < len(arr):
        # calculations for evey increment of j++
        # remove all front elements from help_list which are smaller than arr[j]
        # last element from help_list should be less than or equal to arr[j] and 
        # then push/append the new element into help_list
        while (len(help_list) > 0) and (help_list[-1] <= arr[j]):
            help_list.pop()
        help_list.append(arr[j])

        # try to increase j++ until we get to sub_array size
        if (j-i+1) < k:
            j += 1

        elif (j-i+1) == k:
            # calculate the answer
            # always the greater/max number staying at first index in help_list
            res.append(help_list[0])

            # before slide window
            if arr[i] == help_list[0]:
                # remove the first element from help_list
                help_list.pop(0) # del help_list[0]

            # slide window
            i += 1
            j += 1
    
    return res

print(max_from_sub_array(arr, k))