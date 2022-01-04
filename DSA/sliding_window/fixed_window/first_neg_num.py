# https://www.youtube.com/watch?v=uUXXEgK2Jh8&list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj&index=4
# From the given array find the first negative number from each sub_array

## Input:: arr = [12,-1,-7,8,-15,30,16,28] and k = 3
## Output:: [-1,-1,-7,-15,-15,0] # count:: 6 [len(arr) - k + 1]


arr = [12,-1,-7,8,-15,30,16,28]
k = 3


def first_neg(arr, k):

    # if len(arr) < k then return -1
    if len(arr) < k:
        return -1

    i, j = 0, 0
    neg_list = []
    res = []
    
    while j < len(arr):
        # calculations for evey increment of j++
        # if number is negative then add neg number to neg_list
        if arr[j] < 0:
            neg_list.append(arr[j])

        # try to increase j++ until we get to sub_array size
        if (j-i+1) < k:
            j += 1

        elif (j-i+1) == k:
            # calculate the answer 
            # if neg_list is empty then append "0" to result
            # else append the first element from neg_list and then slide the window
            if len(neg_list) == 0:
                res.append(0)
            else:
                res.append(neg_list[0])
                # before sliding the window compare the "i" with first element from neg_list
                # if equals remove the element from neg_list
                if arr[i] == neg_list[0]:
                    neg_list.pop(0)

            # slide the window
            j+=1
            i+=1

    return res

print(first_neg(arr, k))
