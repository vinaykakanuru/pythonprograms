### Story
## from the given rack of toys you need to pick toys in a sequential order
## and you should only pick two types of toys once you reach two types you need to stop picking

# Find the maximum number of toys can you pick from given rack of toys

## Example ['car', 'elephant', 'car', 'dog', 'car', 'dog'] 
# output: 4 {cars: 2, dogs: 2}

## Input:: main_str = "cecdcd" and k(num of unique char) = 2
## Output:: 4 (cdcd is the longest sub_str with provided num of unique chars)


## Test case 1
main_str = "cecdcd"
k = 2
output = 4

## Test case 2 (We have done the same prob in lon_sub_str_with_unique_char.py)
main_str = "aabacbebebe"
k = 3
output = 7


def pick_toys(main_str, k):
    i, j = 0, 0
    helper_dict = {}
    maxi = 0

    while j < len(main_str):
        # calculations for every increment j++
        # add the char to helper_dict with value as 1 
        # if key already exists increment the char value by 1
        helper_dict[main_str[j]] = helper_dict.get(main_str[j], 0) + 1

        # get the window size till the condition satisfies
        if len(helper_dict.keys()) < k:
            j += 1

        elif len(helper_dict.keys()) == k:
            # find the max window size using (j-i+1)
            maxi = max(maxi, j-i+1)
            j += 1
            
        # slide the window
        elif len(helper_dict.keys()) > k:
            while len(helper_dict.keys()) > k:
                # reduce the count of char at "i" from helper_dict
                helper_dict[main_str[i]] -= 1
                
                # if count of char at "i" becomes zero "0" in helper_dict then remove the key from dict
                if helper_dict[main_str[i]] == 0:
                    helper_dict.pop(main_str[i]) # del helper_dict[main_str[i]]

                i += 1
                
            j += 1
    
    return maxi

print(pick_toys(main_str, k))