"""
a) Given a list of 3 strings, find all combinations (Non-unique and unique, Total 27)
and concatenate each of them.

b) Return the size of largest palindrome substring (Non-circular)
"""

# Example Input:
data =["ab", "baa", "ca"]

"""
Step 1): All 27 combinations
[['ab', 'ab', 'ab'], ['ab', 'ab', 'baa'], ['ab', 'ab', 'ca'],
 ['ab', 'baa', 'ab'], ['ab', 'baa', 'baa'], ['ab', 'baa', 'ca'],
 ['ab', 'ca', 'ab'], ['ab', 'ca', 'baa'], ['ab', 'ca', 'ca'], 
 ['baa', 'ab', 'ab'], ['baa', 'ab', 'baa'], ['baa', 'ab', 'ca'], 
 ['baa', 'baa', 'ab'], ['baa', 'baa', 'baa'], ['baa', 'baa', 'ca'], 
 ['baa', 'ca', 'ab'], ['baa', 'ca', 'baa'], ['baa', 'ca', 'ca'], 
 ['ca', 'ab', 'ab'], ['ca', 'ab', 'baa'], ['ca', 'ab', 'ca'], 
 ['ca', 'baa', 'ab'], ['ca', 'baa', 'baa'], ['ca', 'baa', 'ca'], 
 ['ca', 'ca', 'ab'], ['ca', 'ca', 'baa'], ['ca', 'ca', 'ca']]

Step 2): Concatenate Each Array, then concatenate all even and odd indices
a) ['ababab', 'ababbaa', 'ababca', 
    'abbaaab', 'abbaabaa', 'abbaaca', 
    'abcaab', 'abcabaa', 'abcaca', 
    'baaabab', 'baaabbaa', 'baaabca', 
    'baabaaab', 'baabaabaa', 'baabaaca', 
    'baacaab', 'baacabaa', 'baacaca', 
    'caabab', 'caabbaa', 'caabca', 
    'cabaaab', 'cabaabaa', 'cabaaca', 
    'cacaab', 'cacabaa', 'cacaca']

b) even = "abababababcaabbaabaaabcaababcacabaaabbaabaabaaabbaabaacabaacabaacaababcaabcacabaabaacacaabcacaca"
   odd = "ababbaaabbaaababbaacaabcabaabaaababbaaabcabaabaabaabaacaabbaacacacaabbaacabaaabcabaacacacabaa"

Step 3): Find the largest substring palindrome between both even and odd concatenated strings
Output: "acaabbaacacacaabbaaca" --> len:21

Bonus Step 4) Generate a REST service that allows only POST calls with following logistics:
Input: Array of 3 strings
Output: largest palindrome
"""


# Step 1): All 27 combinations O(n^3) Naive approach to find all the combinations
res = []
for i in range(len(data)):
    for j in range(len(data)):
        for k in range(len(data)):
            inner_res = []
            inner_res.append(data[i])
            inner_res.append(data[j])
            inner_res.append(data[k])
            res.append(inner_res)

print(res)

# Step 2): Concatenate Each Array, then concatenate all even and odd indices
res1 = ["".join(i) for i in res]
print(res1)
    
even = "".join([val for i,val in enumerate(res1) if i%2 == 0])
odd = "".join([val for i,val in enumerate(res1) if i%2 != 0])

print(even)
print(odd)

# Step 3): Find the largest substring palindrome between both even and odd concatenated strings
class Solution(object):
   def longestPalindrome(self, s):
      dp = [[False for i in range(len(s))] for i in range(len(s))]
      for i in range(len(s)):
         dp[i][i] = True
         
      max_length = 1
      start = 0
      for l in range(2,len(s)+1):
         for i in range(len(s)-l+1):
            end = i+l
            if l==2:
               if s[i] == s[end-1]:
                  dp[i][end-1]=True
                  max_length = l
                  start = i
            else:
               if s[i] == s[end-1] and dp[i+1][end-2]:
                  dp[i][end-1]=True
                  max_length = l
                  start = i
      return s[start:start+max_length]

ob1 = Solution()
even_palindrome = ob1.longestPalindrome(even) # baacacaab
odd_palindrome = ob1.longestPalindrome(odd) # acaabbaacacacaabbaaca

print(even_palindrome if len(even_palindrome) > len(odd_palindrome) else odd_palindrome)