"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all 
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and 
numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


Input: s = "race a car"
Output: false
"""


"""
Approach 1 : reverse and compare

- create an empty string : newStr
- for each character in s :
  - check if chaarcter is alphanumeric
  - If Y : add the lower of it to newStr
- return the newStr and reverse of it whether equal
"""

def validPalindrome(s : str) -> bool :
    
    newStr = ""
    for char in s :
        if char.isalphanum() :
            newStr += char.lower()
    return newStr == newStr[::-1]


"""
T(n) : O(n)
S(n) : O(n)
"""

"""
Approach 2 : 2 Pointer

- create a new empty string newStr
- for each char in s :
  - check if char is alphanumeric
  - If Y : add lower of char to newStr  
- l,r =0,last
- while l < r - compare the chars at l,r
- if not same - return F
- in the end return T

"""

def validPalindrome2Pointer(s: str) -> bool :
    newStr = ""
    for char in s :
        if char.isalphanum() :
            newStr += char.lower()
    l,r = 0,len(s) - 1
    while l < r :
        if s[l]!=s[r] :
            return False
        l +=1
        r -=1
    return True

"""
T(n) : O(n)
S(n) : O(1)
"""