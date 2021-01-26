# Input String contains only A and B alphabets in it. Find how many deletions needed to make the given string
# has no same alphabet sits/arranges adjancently.

import re
s = "AABABBABA"  # input

# output should be 2
# because we are removing A at index-0 and B at index-4
# in actual we are not removing we are just comparing how many deletions needed


def alternate_characters(s):
    # method 1 using regular expressions
    # return len(s) - len(re.sub(r'(\w)\1+', r'\1', s))

    # method 2 using typical for loop and summing up all adjancent occurences
    return sum([1 for i in range(len(s)-1) if s[i] == s[i+1]])


print(alternate_characters(s))
