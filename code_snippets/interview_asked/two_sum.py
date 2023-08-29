""" The two sum problem is stated as follows: given an unsorted list and a number S, 
find all the pairs of numbers in that list such that their sum equals S."""

nums = [3, 17, 19, 21, 39]
target = 38

nums = [3, 5, 2, -4, 8,11]
target = 7


# Naive Solution
def naive_solution(arr, target):
    """ The running time complexity for the solution will be O(n^2)
        since we are traversing the list through a nested loop. """
    output = []
    # search first element in the array
    for i in range(len(arr) - 1):
        # search other element in the array
        for j in range(i + 1, len(arr)):
        # if these two elemets sum to pair_sum, print the pair
            if arr[i] + arr[j] == target:
                output.append(f"Pair with sum {target} is: ({arr[i]}, {arr[j]})")
    return output

print(naive_solution(nums, target))

# Optimal Solution
def two_sum(arr, target):
    output = []
    res = {} # 3:3, 17:17, 19:19
    for i in range(len(arr)):
        com = target - arr[i]
        if com in res:
            output.append(f"Pair with sum {target} is: ({arr[i]}, {com})")
        res[arr[i]] = arr[i]
    
    return output

print(two_sum(nums, target))