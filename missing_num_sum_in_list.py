# find the sum of missing number(s) in the given sequence of array/list.

# input array/list
array = [1, 2, 3, 4, 5, 7]
# sample_output: 6

array_1 = [1, 2, 3, 5, 7, 9]
# sample_output: 12

# Summation Approach
# Explanation: find max number and calculate summation (n*(n+1))/2 and find sum of all elements in an array
# and find difference between the values to find the sum of missing numbers in a given sequence


def get_missing_numbers_sum(numbers):
    n = max(numbers)
    total = (n*(n+1))/2
    sum1 = sum(numbers)
    return int(total-sum1)


print('Sum of missing number(s) in the given sequence {} is - {}'.format(array,
                                                                         get_missing_numbers_sum(array)))
print('Sum of missing number(s) in the given sequence {} is - {}'.format(array_1,
                                                                         get_missing_numbers_sum(array_1)))

# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
# Applicable to find single misisng element in given sequence of an array.

# input array/list
numbers = [1, 2, 3, 4, 5, 7]

# sample_output: 6


def get_missing_xor(numbers):
    n = len(numbers)
    x1 = numbers[0]
    for idx in range(1, n):  # applying XOR operation on given array
        x1 = x1 ^ numbers[idx]
    x2 = 0
    for idx in range(1, n+2):  # applying XOR on natural numbers
        x2 = x2 ^ idx

    return x1 ^ x2


print('Missing number in given array {} is - {}'.format(numbers, get_missing_xor(numbers)))
