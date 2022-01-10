""" Normal default BS """

## inputs
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 8


def bs_default_template(arr, target, start=None, end=None):
    """ A normal BS template helps to find the target element in given sorted arr 
    Returns index of the target if present else -1
    """
    start = start if start is not None else 0
    end = end if end is not None else len(arr) - 1

    while(start <= end):
        mid = int(start + (end-start)//2)

        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
        
    return -1 


if __name__ == "__main__":
    print(bs_default_template(arr, target)) ## outputs (7)
