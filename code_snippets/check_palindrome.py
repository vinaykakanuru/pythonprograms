# check the given string can be arranged into a palindrome.

## Note: we are not checking is the given string is a palindrome 
# we are only looking for the chances whether we can arrange the given string into a palindrome.

## Definition:
# ------------
# A set of characters can be arranged as a palindrome 
# only if at most one character from the given string occurs odd number of times
# or all characters frm the given string occurs even number of times.

## Example:
#---------
## Input:: main_str = "vinayaniv" {v:2, i:2, n:2, a:2, y:1}
## Output:: Yes can we can arrange the above string as a palindrome it satisfies the definition.

## Input:: main_str = "aabbbb" {a:2, b:2}
## Output:: Yes can we can arrange the above string as a palindrome as all characters occurs even number of times.


s1 = "vinayaniv" # output:: True
s2 = "aabbbb" # output:: True
s3 = "cdefghmnopqrstuvw" # output:: False
s4 = "(())" # True
s5 = "()((" # False (as two character occurs odd number of times)


def check_palindrome(s):

    # we are checking the count of odd number of characters in the given string it should be always less than 2
    # It should equals 0 or 1 but always less than 2 (check the above palindrome definition)
    return True if len([c for c in set(s) if s.count(c) % 2 != 0]) < 2 else False


print(f'Given String {s1} can become a palindorme? --> {check_palindrome(s1)}')
print(f'Given String {s2} can become a palindorme? --> {check_palindrome(s2)}')
print(f'Given String {s3} can become a palindorme? --> {check_palindrome(s3)}')
print(f'Given String {s4} can become a palindorme? --> {check_palindrome(s4)}')
print(f'Given String {s5} can become a palindorme? --> {check_palindrome(s5)}')