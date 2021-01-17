
arr = [5, 7, 4, 3, 9, 8, 19, 21]
target = 17

# sample_output: (8,9)

# arr = [1, 3]
# target = 4
# sample_output: (8,9)


def pair_with_given_sum(arr, target):
    arr.sort()
    left, right = 0, len(arr)-1
    while (left <= right):
        if arr[left] + arr[right] > target:
            right -= 1
        if arr[left] + arr[right] < target:
            left += 1
        if arr[left]+arr[right] == target:
            return (arr[left], arr[right])


print(pair_with_given_sum(arr, target))
