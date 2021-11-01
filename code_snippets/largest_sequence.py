# to find the largest sequence from a given list/array and
# to return the output as [start number of sequence, end number of the sequence]

# array = [11, 7, 3, 2, 4, 0, 1]  # sample_output = [0,4]
## for the given test case the largest sequence is [0,1,2,3,4] and output should be [0,4]

array = [1, 2, 5, 6, 7]  # sample_output [5,7]
# array = [1,3]  # sample_output [3,3]

## Brute force
# Sort the given array
# go with typical for loop and group all elements which doesn't skip any integer in between two elements
# find the larget group and fetch output as [start, end] of the lagrgest sub_array found
# ---> with this sorted sequence aprach code runs for O(nlog(n)) times to find the output

## Refined Solution
# Explanation: If we use Hashtable like dict in order to check/find the element it normally takes O(1)
# We are creating a hashtable(dict) just like a flag check helper to find the output
# we are trying to check left most and right most of each number by iterating the given array and 
# if left/right numbers are exists in the hasttable(dict) then we are marking their count as "1" and
# if any number from left/right number doesn't exists in dict or say already looked up by the dict value as "1" 
# we are stopped to go beyond left/right extreme edges.
# In this way we can reduce the number of iterations on given array eventually reducing the time complexity.


def largest_range(array):
    numbers = {x: 0 for x in array}
    right = left = 0

    for number in array:
        if numbers[number] == 0:
            left_count = number - 1
            right_count = number + 1

            while left_count in numbers:
                numbers[left_count] = 1
                left_count -= 1
            left_count += 1

            while right_count in numbers:
                numbers[right_count] = 1
                right_count += 1
            right_count -= 1

            if (right-left) <= (right_count-left_count):
                right, left = right_count, left_count

    return [left, right]


print(largest_range(array))
