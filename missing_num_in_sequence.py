# find the missing number in the given sequence of numbers in array/list.
# Applicable to find single misisng element in given sequence of an array.

numbers = [1, 2, 3, 4, 5, 7]

# sample_output: 6

# Summation Approach
# Explanation: find max number and calculate summation (n*(n+1))/2 and find sum of all elements in an array
# and find difference between the values to find missing number in a sequence


def get_missing_summation(numbers):
    n = max(numbers)
    total = (n*(n+1))/2
    sum1 = sum(numbers)
    return int(total-sum1)


print(get_missing_summation(numbers))


def get_missing_xor(numbers):
    n = len(numbers)
    x1 = numbers[0]
    for idx in range(1, n):  # applying XOR operation on given array
        x1 = x1 ^ numbers[idx]
    x2 = 0
    for idx in range(1, n+2):  # applying XOR on natural numbers
        x2 = x2 ^ idx

    return x1 ^ x2


print(get_missing_xor(numbers))
