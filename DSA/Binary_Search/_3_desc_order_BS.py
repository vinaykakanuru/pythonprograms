""" Find the target from sorted (Desc) array using BS """

## inputs
arr = [20, 17, 15, 14, 13, 12, 10, 9, 8, 4]
target = 15

def sorted_array_desc(arr, target):
    start, end = 0, len(arr) - 1

    while(start <= end):
        mid = int(start + (end-start)//2)

        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1 


if __name__ == "__main__":
    print(sorted_array_desc(arr, target)) ## outputs (2)