l = [64, 34, 25, 12, 22, 11, 90]

# Bubble Sort is an easy-to-implement, stable sorting algorithm with a time complexity of O(n²) in the average and worst cases 
# and O(n) in the best case.

# takes list as input and keeps large number at last pos for each comparison

# Check URL: https://www.guru99.com/bubble-sort.html
### Time Complexity
# Worst case – this is where the list provided is in descending order. The algorithm performs the maximum number of executions which is expressed as [Big-O] O(n2)
# Best case – this occurs when the provided list is already sorted. The algorithm performs the minimum number of executions which is expressed as [Big-Omega] ?(n)
# Average case – this occurs when the list is in random order. The average Complexity is represented as [Big-theta] ?(n2)

### Space Complexity
# The space complexity measures the amount of extra space that is needed for sorting the list. 
# The bubble sort only requires one (1) extra space for the temporal variable used for swapping values. 
# Therefore, it has a space complexity of O (1).

### Normal Bubble Sort
def bubble_sort(list):
    for i in range(len(l)-1, 0, -1):  # keep large number at last
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

print('Bubble Sort: ', bubble_sort(l))


### optimized bubble sort
def optimized_bubble_sort(list):
    ## (n-1) Number of passes happening for given n size array
    for i in range(len(l)-1, 0, -1):
        no_swap_flag = 0 # flag to check if there is any swap happening in compare loop
        
        ## actual value compare loop
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                no_swap_flag = 1
        
        ## breaking the passes 
        if no_swap_flag == 0:
            break
            
    return list

print('optimized_bubble_sort: ', optimized_bubble_sort(l))
