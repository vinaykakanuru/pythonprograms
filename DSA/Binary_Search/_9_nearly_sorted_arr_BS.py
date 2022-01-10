arr = [5, 10, 30, 20, 40]
target = 20

def nearly_sorted_array_bs(arr, target):
    start, end = 0, len(arr) - 1
    
    while (start <= end):
        mid = int(start + (end - start)//2)
        print(f"start:: {start}, end:: {end}, mid:: {mid}")
        
        if arr[mid] == target:
            return mid
        elif (mid-1) >= start and target == arr[mid-1]:
            return mid - 1
        elif (mid+1) <= end and target == arr[mid+1]:
            return mid + 1
        elif target < arr[mid]:
            end = mid - 2
        else:
            start = mid + 2
        

print(nearly_sorted_array_bs(arr, target))