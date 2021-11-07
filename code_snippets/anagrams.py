## anagram simple satisfactory conditions
# 1) new_sub_str should be of same length of a given sub_str
# 2) Each character should be in same quantity in both sub_str and new_sub_str

## Input:: s1 = "aaab" and s2 = "aaba"
## Output:: both strings of same length

# Test case 1
s1 = "aaab"
s2 = "aaba"

# Test case 2
s3 = "aaaba"
s4 = "aaba"


def is_anagrams(a, b):
    # if both lenghths are not matched return False and go for following check
    if len(a) != len(b):
        return False
    
    # checking both the given strings in sorted way 
    if sorted(a) == sorted(b):
        return True

print(f'Given Strings "{s1}", "{s2}" are anagrams? --> {is_anagrams(s1, s2)}')
print(f'Given Strings "{s3}", "{s4}" are anagrams? --> {is_anagrams(s3, s4)}')
