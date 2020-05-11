l = [64, 34, 25, 12, 22, 11, 90]


# In selection sort we start by finding the minimum value in a given list and move it to a sorted list.
# Then we repeat the process for each of the remaining elements in the unsorted list.
# The next element entering the sorted list is compared with the existing elements and placed at its correct position

def selection_sort(list):
    for idx in range(len(list)):
        min_idx = idx
        for j in range(idx + 1, len(list)):
            if list[min_idx] > list[j]:
                min_idx = j
        # Swap the minimum value with the compared value
        list[idx], list[min_idx] = list[min_idx], list[idx]    
    return list

print(selection_sort(l))

