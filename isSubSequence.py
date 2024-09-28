"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

Input: s = "abc", t = "ahbgdc"
Output: true

Input: s = "axc", t = "ahbgdc"
Output: false

"""

def isSubsequence(s: str, t: str) -> bool:
    sptr = 0

    for i in range(len(t)) :
        if sptr < len(s):
            if s[sptr] == t[i]:
                sptr += 1
    
    return sptr == len(s)


s = "b"
t = "ahbgdc"

output = isSubsequence(s,t)
print(output)


"""
S(n) -> O(n)
T(n) -> O(1)

"""