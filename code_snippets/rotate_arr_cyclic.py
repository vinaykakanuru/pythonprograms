""" 
Need to rotate the given array elements with the given k places for n times 
and print K elements for each iteration 
"""

## input
arr = [1,2,3,4,5,6]
k = 4 
n = 7 # 7 times we need to rotate the given array

## output
# [1, 2, 3, 4]
# [5, 6, 1, 2]
# [3, 4, 5, 6]
# [1, 2, 3, 4]
# [5, 6, 1, 2]
# [3, 4, 5, 6]
# [1, 2, 3, 4]

def rotate_arr(arr, k, n):
    for _ in range(n):
        print(arr[:k]) # prints K elements for every iteration
        arr = arr[k:] + arr[:k] # rotating the arr elements for given K places

if __name__ == "__main__":
    rotate_arr(arr, k, n)