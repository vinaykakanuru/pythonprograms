arr = [1, 2, 3, 4, 8, 10, 10, 12, 19] 
target = 5

def floor_bs(arr, target):
    start, end = 0, len(arr) - 1
    res = -1
    
    while (start <= end):
        mid = int(start + (end - start)//2)
        print(f"start:: {start}, end:: {end}, mid:: {mid}")
        
        if target == arr[mid]:
            return mid

        if arr[mid] < target:
            res = mid
            start = mid + 1

        if arr[mid] > target:
            end = mid - 1

        print(f"res:: {res}")
    return res

print(floor_bs(arr, target))