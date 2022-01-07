normal_sorted_arr = [2, 5, 6, 8, 11, 12, 15, 18]
rotated_sorted_arr = [11, 12, 15, 18, 2, 5, 6, 8]

def num_of_times_rotated(arr):
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

        if arr[start] <= arr[mid]:
            start = mid + 1

        if arr[mid] <= arr[end]:
            end = mid - 1


print(num_of_times_rotated(rotated_sorted_arr))