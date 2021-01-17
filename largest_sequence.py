# to find largest sequence in a given list/array and
# to return output of start number of sequence and end number of the sequence

# array = [11, 7, 3, 2, 4, 0, 1]  # sample_output = [0,4]
array = [1, 2, 5, 6, 7]  # sample_output [5,7]
# array = [1,3]  # sample_output [3,3]


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
