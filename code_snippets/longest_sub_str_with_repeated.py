""" Find the longest sub string with repeated characters present in the given input string """

"""
Explanation:

In the given input string find the longest substring (which is formed by the same char).
Focus on the next/beside element with travesral element whether both are same then increase the counter.
Otherwise restart the counter. For every restart of the counter keep the max length into one res container.

"""
str = "aaabbbbccccccdddddeeeeeaaaaaaaahhhhh"
# output: 8 (aaaaaaaa) longest sub str with repeated char 

def find_longest_sub_str(str):
    """ Takes string as input and returns an integer """
    if len(str) == 0:
        return "Please provide a valid string with atleast one char"
    
    # support variables initializing with value one. 
    # Considering the i/p str is not empty and atleast one char present in it.
    res, counter = 1, 1

    for idx in range(1, len(str)):
        if str[idx] == str[idx-1]:
            counter += 1
        else:
            res = max(res, counter)
            counter = 1
    
    return res

if __name__ == "__main__":
    print(find_longest_sub_str(str))
    print(find_longest_sub_str("abccd"))