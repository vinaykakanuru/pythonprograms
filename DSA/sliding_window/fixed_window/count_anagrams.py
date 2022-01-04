## https://www.youtube.com/watch?v=MW4lJ8Y0xXk&list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj&index=5

# Count occureneces of anagrams of a given sub_string in a given main_string

## Input:: main_str = "aabaabaa" and sub_str = "aaba"
## Output:: 4


## anagram simple satisfactory conditions
# 1) new_sub_str should be of same length of sub_str
# 2) Each character should be in same quantity in sub_str and new_sub_str
# Example: anagrams for "aaba" are ["aaab", "baaa", "abaa"]


# so for every window we are cheking the anagram conditions if all anagram conditions matches the we increase our counter

### brute force technique 
# find all combinations of anagrams (k! factorial) and search each anagram in given main string
# Time complexity will be worst than sliding window (worst time complexity of sliding windows is O(n))

# Test case 1
main_str = "aabaabaa"
sub_str = "aaba"
output = 4

# Test case 2
# main_str = "forxxorfxdofr"
# sub_str = "for"
output = 3

# Test case 3
# main_str = "aabaaaba"
# sub_str = "ab"
output = 4

from collections import Counter

def count_anagrams(main_str, sub_str):
    # if len(main_str) < len(sub_str) then return -1
    if len(main_str) < len(sub_str):
        return -1

    k = len(sub_str) # window size equals to len(sub_str)
    i, j = 0, 0 # index variables
    d = Counter(sub_str) # helper dict with distinct char with counts from given sub_str
    unique_char_count = len(d.keys()) # count var helps to find the result
    res = 0

    while j < len(main_str):
        # initial calculations for evey increment of j++
        # if main_str[j] in dictionary, decrement the count of main_str[j] by 1 and 
        # if the main_str[j] count equals zero decrement unique_char_count by 1
        if main_str[j] in d.keys():
            d[main_str[j]] -= 1
        
            # decrement the unique_char_count by 1 only if "any distinct" char count becomes zero
            if d[main_str[j]] == 0:
                unique_char_count -= 1

        # try to increase j++ until we get to sub_str size
        if (j - i + 1) < k:
            j += 1

        # if we reach proper window_size then do calculations and slide window
        elif (j -i + 1) == k:
            # calculations 
            # if unique_char_count equals zero that means all distinct char counts from the give sub_str becomes zero
            # that means our current window is made up of an anagram from given sub_str
            if unique_char_count == 0:
                res += 1

            # before sliding calculations for 'i' increment i++
            # increment the char count in dict by 1 and if any distinct char count crosses above zero margin
            # then increment unique_char_count by 1
            if main_str[i] in d.keys():
                d[main_str[i]] += 1

                if d[main_str[i]] == 1:
                    unique_char_count += 1

            # slide window
            i += 1
            j += 1
    
    return res

print(count_anagrams(main_str, sub_str))