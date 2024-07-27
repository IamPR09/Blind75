"""
Given a string s, return the longest palindromic substring in s.

Input: s = "babad"
Output: "bab"

"""

"""
Approach 1 : 2 Pointer inside Out

- 2 variables
 - maxLen
 - resStr

- for each char :
  - initiate two pointers at this position
   - boundary check - l > 0, r < len(s) and char[l] == char[s]
    - if (r-l + 1) is greater than maxlen :
       - res = s[l:r+1]
       - maxLen = (l-r) + 1
      - decrement l
      - increment r
  - initiate two pointers one at i, one at i+1

"""

def longestPalindrome(s : str) :
    resStr = ""
    maxLen = 0

    for i in range(len(s)) :
        l,r = i,i
        while l >= 0 and r < len(s) and s[l] == s[r] :
            if (r - l + 1) > maxLen :
                maxLen = (r - l) + 1
                resStr = s[l : r+1]
            l -= 1
            r += 1

        l,r = i, i+1
        while l > 0 and r < len(s) and s[l] == s[r]:
            if (r - l) + 1 > maxLen :
                maxLen = (r - l) + 1
                resStr = s[l : r+1]
            l -= 1
            r += 1
    return resStr

s = "cbbd"
ans = longestPalindrome(s)
print(ans)
    
    