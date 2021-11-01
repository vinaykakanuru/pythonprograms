## variable window size problem (need to find the window size --> max/min or some other satisifying condition)

# from the given Array find the length of largest sub_array which gives us provided sum (condition)

## Input:: arr = [4, 1, 1, 1, 2, 3, 5] and k(sum) = 5
## Output:: 4

## Test case 1
arr = [4, 1, 1, 1, 2, 3, 5]
k = 5
output = 4

## Test case 2
arr = [4, 2, 2, 1, 2, 3, 5]
k = 6
output = 3

## Test case 3
arr = [1, 2, 3, 7, 5]
k = 12
output = 3


def largest_sub_array(arr, k):
    i, j = 0, 0
    sums = 0
    maxi = 0
    
    while j < len(arr):
        # calculations for every increment j++
        sums = sums + arr[j]

        # get the window size till the condition satisfies
        if sums < k:
            j += 1

        elif sums == k:
            # find the max window size using (j-i+1)
            maxi = max(maxi, j-i+1)
            j += 1
            
        # slide the window
        elif sums > k:
            while sums > k: # 13 > 12
                sums = sums - arr[i] # 13 - 1, 12
                i += 1
                
                # edge case scenario found for Test case 3
                if sums == k:
                    maxi = max(maxi, j-i+1)
                    break
            
            j += 1
            
    return maxi


print(largest_sub_array(arr, k))