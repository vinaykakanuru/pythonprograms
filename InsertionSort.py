l = [19,2,31,45,30,11,121,27]

# Insertion sort involves finding the right place for a given element in a sorted list
# So in beginning we compare the first two elements and sort them by comparing them.
# Then we pick the third element and find its proper position among the previous two sorted elements.
# This way we gradually go on adding more elements to the already sorted list by putting them in their proper position.

def insertion_sort(list):
    for i in range(1, len(list)):
        j = i - 1
        nxt_element = list[i]
        # Compare the current element with next one

        while (list[j] > nxt_element) and (j >= 0):
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = nxt_element
    return list


print('insertion sort: ', insertion_sort(l))