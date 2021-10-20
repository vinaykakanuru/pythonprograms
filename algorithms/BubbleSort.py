l = [64, 34, 25, 12, 22, 11, 90]

# Bubble Sort is an easy-to-implement, stable sorting algorithm with a time complexity of O(n²) in the average and worst cases 
# and O(n) in the best case.

# takes list as input and keeps large number at last pos for each comparison

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
