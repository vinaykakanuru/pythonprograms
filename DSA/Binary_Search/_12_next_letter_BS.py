""" Find the Next alphabet from given sorted array of alphabets """

## inputs
arr = ['a', 'c', 'f', 'g', 'h']
target = 'f'


def next_letter_bs(arr, target):
    start, end = 0, len(arr) - 1
    res = -1

    while (start <= end):
        mid = int(start + (end - start)/2) 

        # as we need the next alphabet we need to look further even though elem find at mid value
        if ord(arr[mid]) == ord(target): 
            start = mid + 1

        if ord(arr[mid]) > ord(target):
            res = mid
            end = mid - 1

        if ord(arr[mid]) < ord(target):
            start = mid + 1
    return res


# output index of next alphabet target (3)
print(f"Ceil of {target} from given sorted array: ", next_letter_bs(arr, target))

# output index of next alphabet target (1)
print(f"Ceil of 'a' from given sorted array: ", next_letter_bs(arr, 'a'))

# output index of next alphabet target (-1)
print(f"Ceil of 'h' from given sorted array: ", next_letter_bs(arr, 'h'))