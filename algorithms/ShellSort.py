l = [64, 34, 25, 12, 22, 11, 90]


# We sort a large sublist of a given list and go on reducing the size of the list until all elements are sorted.
# The below program finds the gap by equating it to half of the length of the list size and then starts sorting all elements in it.
# Then we keep resetting the gap until the entire list is sorted.

'''
The worst-case of your implementation is Θ(n^2) and the best-case is O(nlogn) which is reasonable for shell-sort.

##The best case ∊ O(nlogn):
The best-case is when the array is already sorted. The would mean that the inner if statement will never be true, 
making the inner while loop a constant time operation. Using the bounds you've used for the other loops gives O(nlogn). 
The best case of O(n) is reached by using a constant number of increments.

##The worst case ∊ O(n^2):
Given your upper bound for each loop you get O((log n)n^2) for the worst-case. 
But add another variable for the gap size g. The number of compare/exchanges needed in the inner while is now <= n/g. 
The number of compare/exchanges of the middle while is <= n^2/g. Add the upper-bound of the number of compare/exchanges for each gap together: n^2 + n^2/2 + n^2/4 + ... <= 2n^2 ∊ O(n^2). 
This matches the known worst-case complexity for the gaps you've used.

##The worst case ∊ Ω(n^2):
Consider the array where all the even positioned elements are greater than the median. 
The odd and even elements are not compared until we reach the last increment of 1. 
The number of compare/exchanges needed for the last iteration is Ω(n^2).
'''

'''
The worse-case time complexity of shell sort depends on the increment sequence. 
For the increments 1 4 13 40 121…, which is what is used here, the time complexity is O(n3/2). 
For other increments, time complexity is known to be O(n4/3) and even O(n·lg2(n)). 
Neither tight upper bounds on time complexity nor the best increment sequence are known.

Because shell sort is based on insertion sort, shell sort inherits insertion sort’s adaptive properties. 
The adapation is not as dramatic because shell sort requires one pass through the data for each increment, but it is significant. 
For the increment sequence shown above, there are log3(n) increments, so the time complexity for nearly sorted data is O(n·log3(n)).

Because of its low overhead, relatively simple implementation, adaptive properties, and sub-quadratic time complexity, 
shell sort may be a viable alternative to the O(n·lg(n)) sorting algorithms for some applications when the data to be sorted is not very large.

## Properties
-> Not stable
-> O(1) extra space
-> O(n3/2) time as shown (see below)
-> Adaptive: O(n·lg(n)) time when nearly sorted
'''


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
