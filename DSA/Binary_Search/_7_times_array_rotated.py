normal_sorted_arr = [2, 5, 6, 8, 11, 12, 15, 18]
rotated_sorted_arr = [12, 15, 18, 2, 5, 6, 8, 11]

def num_of_times_rotated(arr):
    """ Finding the index of a minimun element from rotated sorted array 
    to find how many times the sorted array is rotated
    """
    start, end = 0, len(arr) - 1
    n = len(arr)

    while (start <= end):
        mid = int(start + (end - start)/2)

        ## because we are perfoming calculations on rotated sorted array 
        # and if we are at last index how can we find next, next elem should be starting of the array
        # and if we are at first index how can we find prev, prev elem should be last elem of the array

        next_elem = (mid + 1) % n
        prev_elem = (mid + n - 1) % n

        if arr[mid] <= arr[next_elem] and arr[mid] <= arr[prev_elem]:
            return mid

        if arr[0] <= arr[mid]:
            start = mid + 1

        if arr[mid] <= arr[-1]:
            end = mid - 1

    return -1


if __name__ == "__main__":
    ## outputs index of min element from the given rotated sorted array (3)
    print(num_of_times_rotated(rotated_sorted_arr)) 