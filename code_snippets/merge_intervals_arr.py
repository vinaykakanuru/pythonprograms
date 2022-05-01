""" 
Merge the Sub array elements consists of some intervals (a,b) where a < b always. 
Output is in any order of sub array elements
"""

## input 
arr = [[10, 15], [18, 25], [14, 20], [3, 5], [7, 9]]

## output
# [[3, 5], [7, 9], [10, 25]]


# Solution:
# 1) Sort the sub arr elements in ascending order based on first element
# 2) Create one helper variable to store the result and store the first sub_arr into res
# 3) Loop over the main arr from 1 to end of the array
# 4) Apply greater check operation on the "b" last sub array element of res[-1][1] 
#     with "a" of iterative sub array element of main arr i.e arr[i][0]
# 5) If greater merge the sub arrays i.e res[-1][1] = arr[i][1]
# 6) Else treat the sub_arr of iterative main arr element doesn't have the common intreval to merge

def merge_intervals(arr):
    arr.sort(key = lambda x: x[0])
    print(f"Sorted array: {arr}")

    res = [arr[0]]
    for i in range(1, len(arr)):
        if res[-1][1] > arr[i][0]:
            res[-1][1] = arr[i][1]
        else:
            res.append(arr[i])
    
    return res

if __name__ == "__main__":
    print(f"Merge Intervals for the given arr: {arr} is:: \n{merge_intervals(arr)}")