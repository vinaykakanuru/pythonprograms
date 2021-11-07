# We need to check if the given string can be Converted as a Palindrome 
# just by changing one character from the given string


s1 = "abccaa"  # True [can change into palindrome by changing 'a' to 'b']
s2 = "abbcca"  # False [can't convert this string to a palindrome by changing a single character]
s3 = "vinayaniv"  # already a palindrome string should return True


def str_to_palindrome(s):

    n = len(s)  # declaring variable with length of the given string

    # finding the sum of characters which does not match on both half sides of the string
    count = sum([1 for i in range(0, n//2) if s[i] != s[n-i-1]])

    # count<=1 states that if less than single character conversion can meets the requirement
    return True if count <= 1 else False


print(f'Given String {s1} is a palindorme? --> {str_to_palindrome(s1)}')
print(f'Given String {s2} is a palindorme? --> {str_to_palindrome(s2)}')
print(f'Given String {s3} is a palindorme? --> {str_to_palindrome(s3)}')