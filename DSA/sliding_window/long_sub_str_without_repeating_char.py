# https://www.youtube.com/watch?v=L6cffskouPQ&list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj&index=11&ab_channel=AdityaVerma
# Find the longest sub_str form given main_str with no repeating char (without char repetition)

## Input:: main_str = "pwwkew"  and condition: (No repeating char) --> (All unique chars in a given window)
## Output:: 3 (wke/kew are the longest sub_strings/windows with all unique chars (no char repetition))

## Test case 1
main_str = "pwwkew"
output = 3

## Test case 2
main_str = "pwwkewf"
output = 4 # (kewf) is the longest sub_str with all unique chars in a given window

## Test case 3
main_str = "pwwfgkewf"
output = 5 # (wfgke) is the longest sub_str with all unique chars in a given window


def long_sub_str_without_repeating_char(main_str):
    i, j = 0, 0
    helper_dict = {}
    maxi = 0

    while j < len(main_str):
        # calculations for every increment j++
        # add the char to helper_dict with value as 1 
        # if key already exists increment the char value by 1
        helper_dict[main_str[j]] = helper_dict.get(main_str[j], 0) + 1

        # for the given business requirement and as per varibale sliding window format 
        # we don't need this j++ check as we are not given with K(related cond to window size)
        # get the window size till the condition satisfies
        # if len(helper_dict.keys()) < j-i+1:
        #     j += 1

        if len(helper_dict.keys()) == j-i+1:
            # find the max window size using (j-i+1)
            maxi = max(maxi, j-i+1)
            j += 1
            
        # slide the window
        elif len(helper_dict.keys()) < j-i+1:
            while len(helper_dict.keys()) < j-i+1:
                # reduce the count of char at "i" from helper_dict
                helper_dict[main_str[i]] -= 1
                
                # if count of char at "i" becomes zero "0" in helper_dict then remove the key from dict
                if helper_dict[main_str[i]] == 0:
                    helper_dict.pop(main_str[i]) # del helper_dict[main_str[i]]

                i += 1
                
            j += 1
    
    return maxi


print(long_sub_str_without_repeating_char(main_str))