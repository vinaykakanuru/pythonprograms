# To check the given two strings are equal by adjusting N characters.

s1 = "Github code snippets"
s2 = "github code snippets"

# Will find how many characters needs to be adjusted, for equal strings.
def compare(s1, s2):
    """ comparing each character from both strings with index """
    return sum(s1[i] != s2[i] for i in range(len(s1))) <= 1

print(compare(s1, s2))

s3 = "Github code snippets."
s4 = "github code snippets"

# Will find how many characters needs to be adjusted, for different length strings.
def match(s1, s2):
    l = min(len(s1), len(s2))
    return sum(s1[i] != s2[i] for i in range(l)) + abs(len(s1) - len(s2)) <= 1

# returns False as two charcters 'G', '.' needs to be adjusted to make both strings matched.
# we are trying to find only for one Change. 
print(match(s3, s4)) 