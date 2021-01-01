l = [64, 34, 25, 12, 22, 11, 90]


# We sort a large sublist of a given list and go on reducing the size of the list until all elements are sorted.
# The below program finds the gap by equating it to half of the length of the list size and then starts sorting all elements in it.
# Then we keep resetting the gap until the entire list is sorted.

def shell_sort(list):
    gap = len(list) // 2
    while gap > 0:
        for i in range(gap, len(list)):
            temp = list[i]
            j = i
            # Sort the sub list for this gap
            while j >= gap and list[j - gap] > temp:
                list[j] = list[j - gap]
                j = j - gap
            list[j] = temp

        # Reduce the gap for the next element
        gap = gap // 2
    return list


print('Shell Sort: ', shell_sort(l))
