""" Find last occurence of an elemnet to be searched in sorted array """

## inputs
arr = [2, 4, 10, 10, 10, 18, 20]
target = 10


def first_occurence_sorted_arr(arr, target, start=None, end=None):
    start = start if start is not None else 0
    end = end if end is not None else len(arr) - 1
    res = -1

    while(start <= end):
        mid = int(start + (end-start)//2)

        if target == arr[mid]:
            res = mid
            end = mid - 1
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return res


def last_occurence_sorted_arr(arr, target, start=None, end=None):
    start = start if start is not None else 0
    end = end if end is not None else len(arr) - 1
    res = -1

    while(start <= end):
        mid = int(start + (end-start)//2)

        if target == arr[mid]:
            res = mid
            start = mid + 1
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return res



if __name__ == "__main__":
    print(f"First Occurence of {target} is at:: ", first_occurence_sorted_arr(arr, target)) ## outputs (2)
    print(f"Last Occurence of {target} is at:: ", last_occurence_sorted_arr(arr, target)) ## outputs (4)