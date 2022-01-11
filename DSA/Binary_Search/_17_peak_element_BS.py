""" Peak element """

## inputs
arr = [5, 10, 20, 15]

def peak_element(arr):
    start, end = 0, len(arr) - 1
    while (start <= end):
        mid = int(start + (end - start)//2)

        # if mid is at start/end pos, don't check for neighbor comparison
        if (mid > 0 and mid < len(arr) - 1):
            if (arr[mid] > arr[mid - 1]) and (arr[mid] > arr[mid + 1]):
                return mid
            elif arr[mid - 1] > arr[mid]:
                end = mid - 1
            elif arr[mid + 1] > arr[mid]:
                start = mid + 1
        
        # handling Edge cases while mid is at either start/end position
        if (mid == 0):
            if arr[0] > arr[1]:
                return 0
            else:
                return 1
        if (mid == len(arr) - 1):
            if arr[len(arr) - 1] > arr[len(arr) - 2]:
                return len(arr) - 1
            else:
                return len(arr) - 2


if __name__ == "__main__":
    print(peak_element(arr)) # outputs (2)
    print(peak_element([10, 20, 15, 2, 23, 90, 67])) # outputs (1)
    print(peak_element([1, 3, 8, 12, 4, 2])) # outputs (3)