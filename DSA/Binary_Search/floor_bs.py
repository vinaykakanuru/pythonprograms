arr = [1, 2, 3, 4, 4.4, 8, 10, 10, 12, 19] 
target = 4.6

def floor_bs(arr, target):
    start, end = 0, len(arr) - 1
    res = -1
    
    while (start <= end):
        mid = int(start + (end - start)//2)
        print(f"start:: {start}, end:: {end}, mid:: {mid}")
        
        if target == arr[mid]:
            return mid

        if target < arr[mid]:
            res = mid
            end = mid - 1

        if target > arr[mid]:
            start = mid + 1

        print(f"res:: {res}")
    return res

print(floor_bs(arr, target))