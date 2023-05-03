# To check the given two strings are equal by adjusting N characters.

s1 = "Github code snippets"
s2 = "github code snippets"

s3 = "Github code snippets."
s4 = "github code snippets"

s5 = "Geeks for Geeks."
s6 = "geeks 4 geeks"

def compare(s1, s2):
    """ return num of characters needs to be adjusted to make both strings equal """
    # Will find how many characters needs to be adjusted, for equal length of strings.
    if len(s1) == len(s2):
        return sum(s1[i] != s2[i] for i in range(len(s1)))
    else:
        # Will find how many characters needs to be adjusted, for different length strings.
        l = min(len(s1), len(s2))
        return sum(s1[i] != s2[i] for i in range(l)) + abs(len(s1) - len(s2))


print(compare(s1, s2)) # 1
print(compare(s3, s4)) # 2
print(compare(s5, s6)) # 11 # actual expected is 6 characters nees to be adjusted

# --------------------Solving edge case using below function--------------------------#
""" Even if the strings are of equal lengths or not if characters shuffle in the given strings 
above solution cannot handle to count how many characters needs to be adjusted. Since above solutions
checking the characters in both the stings using left to right approach using index."""

def eval_strings(s1, s2):
    """ returns number of characters needs to be adjusted to make both strings equal """
    # assuming s1 always less than s2 swapping if s1 > s2 
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    return sum(1 for i in s1 if s2.count(i) == 0) + abs(len(s1) - len(s2))

print(eval_strings(s1, s2)) # 1
print(eval_strings(s3, s4)) # 2
print(eval_strings(s5, s6)) # 6
