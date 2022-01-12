""" Allocate minimum number of pages """

## inputs
arr = [10, 20, 30, 40]
target = 2


def is_valid(arr, arr_size, target, mx):
    student = 1
    sum_ = 0
    for i in range(arr_size):
        sum_ = sum_ + arr[i]
        if sum_ > mx:
            student += 1
            sum_ = arr[i]
        
        if student > target:
            return False

    return True


def allocate_min_pages_of_book(arr, target):
    if len(arr) < target:
        return -1 

    start = max(arr)
    end = sum(arr)
    res = -1
   
    while(start <= end):
        mid = int(start + (end-start)//2)
        if is_valid(arr, len(arr), target, mid) == True:
            res = mid
            end = mid - 1
        else:
            start = mid + 1
    return res


if __name__ == "__main__":
    print(allocate_min_pages_of_book(arr, target)) ## outputs ()