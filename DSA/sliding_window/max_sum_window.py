# From the given array find the max sum from the provided fixed window size

## Input:: arr = [2,5,1,8,2,9,1] and k = 3
## Output:: 19


arr = [2,5,1,8,2,9,1]
k = 3

def find_max_sum(arr, k):
    n = len(arr)

    # arr size must be greater than given sub_array k
    if n < k:
        return -1

    # Compute sum of first window of size k
    window_sum = sum(arr[:k])

    # first sum available
    max_sum = window_sum

    # Compute the sums of remaining windows by
    # removing first element of previous window and adding last element of the current window.
    for i in range(n-k):
        window_sum = window_sum - arr[i] + arr[i+k]
        max_sum = max(window_sum, max_sum)
    
    return max_sum


# print(find_max_sum(arr, k))

## https://www.youtube.com/watch?v=KtpqeN0Goro&list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj&index=3
def max_sum(arr, k):
    # if len(arr) < k then return -1
    if len(arr) < k:
        return -1

    i, j = 0, 0
    sums = 0
    max_sum = 0

    while j < len(arr):
        # initial calculations for evey increment of j++
        sums = sums + arr[j]

        # try to increase j++ until we get to sub_array size
        if (j-i+1) < k:
            j += 1
        
        elif (j-i+1) == k:
            # do calculation on the window size array elements
            max_sum = max(max_sum, sums)
            sums = sums - arr[i]
        
            # slide the window
            i += 1
            j += 1
    
    return max_sum

print(max_sum(arr, k))
        

