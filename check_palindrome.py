# check the given string is palindrome or whether the given string can be arranged into a palindrome

# A set of characters can form a palindrome if at most one character occurs odd number of times
# and all characters occur even number of times.

s1 = "vinayaniv"
s2 = "aaabbbb"
s3 = "cdefghmnopqrstuvw"


def check_palindrome(s):

    # we are checking the count of odd number of characters in the given string it should be always less than 2
    # It should equals 0 or 1 but always less than 2 (check the above palindrome definition)
    return True if len([c for c in set(s) if s.count(c) % 2 != 0]) < 2 else False


print(check_palindrome(s1))