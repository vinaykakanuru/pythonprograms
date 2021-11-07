# We need to check if the given string can be Converted as a Palindrome 
# just by changing one character from the given string


s1 = "abccaa"  # True [can change into palindrome by changing 'a' to 'b']
s2 = "abbcca"  # False [can't convert this string to a palindrome by changing a single character]
s3 = "vinayaniv"  # already a palindrome string should return True


def is_palindrome(s):
    return True if s == s[::-1] else False


def str_to_palindrome(s):
    n = len(s)  # declaring variable with length of the given string

    ## optimizing the given string parsing. 
    # If already a palindrome ignore the following check and returns True
    # Else go for following check
    if is_palindrome(s):
        return True
    
    # finding the sum of characters which does not match on both half sides of the string
    # sum <= 1 states that if less than single character conversion can meets the requirement
    return True if sum([1 for i in range(0, n//2) if s[i] != s[n-i-1]]) <= 1 else False


print(f'Given String {s1} can be a palindorme? --> {str_to_palindrome(s1)}')
print(f'Given String {s2} can be a palindorme? --> {str_to_palindrome(s2)}')
print(f'Given String {s3} can be a palindorme? --> {str_to_palindrome(s3)}')