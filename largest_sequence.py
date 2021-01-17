# to find largest sequence in a given list/array and
# to return output of start number of sequence and end number of the sequence

# array = [11, 7, 3, 2, 4, 0, 1]  # sample_output = [0,4]
array = [1, 2, 5, 6, 7]  # sample_output [5,7]
# array = [1,3]  # sample_output [3,3]

# Explanation: If we use Hashtable like dict to check the elements it takes O(1)
# we are trying to check left most and right most of each number from given array and if number is found in given
# array we are marking it's value as 1 in HashTable/dict and for the next loop we are checking those numbers
# who has value 0 from HashTable/dict

# If we try to sort the given array and find the missing element from the sorted sequence it runs nlog(n) times


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
