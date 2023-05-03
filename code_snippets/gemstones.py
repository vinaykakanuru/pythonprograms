# find the common alphabets present in the given array of strings

# input
arr = ['abcde', 'bcde', 'cfgh']

# output should be 'c' because 'c' is the common alphabet present in all elements in the given array

# method 1 using set
def gemstones_method_1(arr):
    arr1 = [set(i) for i in arr]
    return set.intersection(*arr1)


print(gemstones_method_1(arr))


# method 2 using ascii_lowercase
def gemstones_method_2(arr):
    from string import ascii_lowercase
    all_chars = set(ascii_lowercase)
    for i in arr:
        all_chars = all_chars.intersection(set(i))
        print(all_chars)
    return all_chars


print(gemstones_method_2(arr))
