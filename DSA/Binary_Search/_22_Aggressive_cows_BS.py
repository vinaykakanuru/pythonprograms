""" Aggressive Cows """

## inputs
arr = [1, 2, 4, 8, 9]
cows = 3


def is_valid(arr, n, cows, dist):
    count = 1
    cow_ord = arr[0]
    for i in range(1, n):
        if arr[i] - cow_ord >= dist:
            count += 1
            cow_ord = arr[i]
        if count == cows:
            return True

    return False


def aggressive_cows(arr, cows):
    start = 1
    end = arr[-1] - arr[0]
    res = -1

    while (start <= end):
        mid = int(start + (end - start)//2)

        if (is_valid(arr, len(arr), cows, mid)) == True:
            res = mid
            start = mid + 1 
        else:
            end = mid - 1
    
    return res


if __name__ == "__main__":
    print(aggressive_cows(arr, cows)) ## outputs (3)