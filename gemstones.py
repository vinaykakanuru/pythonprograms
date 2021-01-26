# find the common alphabets present in the given array of strings

# input
arr = ['abcde', 'bcde', 'cfgh']

# output should be 'c' because 'c' is the alphabet present in all elements in the given array


def gemstones(arr):
    # method 1
    arr1 = [set(i) for i in arr]
    return set.intersection(*arr1)

    # method 2 using ascii_lowercase
    # from string import ascii_lowercase
    # all_chars = set(ascii_lowercase)
    # for i in arr:
    #     all_chars = all_chars.intersection(set(i))
    # return all_chars


print(gemstones(arr))
