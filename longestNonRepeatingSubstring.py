"""
Given a string s, find the length of the longest substring without repeating characters

Input: s = "abcabcbb"
Output: 3
"""

"""
Approach 1 : Looping

 - initiate maxLen = 0
 - for each character:
   - set count = 1
   - initiate a set/map
   - add the character if doesnt exist
     - increment the count
   - if exists :
     - break
 - update maxLen = max(maxLen, count)

"""

def longthOfLongestSubstringLoop(s : str) -> int :
    maxLen = 0
    for i in range(len(s)) :
        currentCount = 0
        charSet = set()
        for j in range(i,len(s)) :
            if s[j] not in charSet :
                charSet.add(s[j])
                currentCount += 1
            else :
                break
        maxLen = max(currentCount, maxLen)
    return maxLen


s = "pwwkew"

#ans = longthOfLongestSubstringLoop(s)
#print(ans)


"""
T(n) : O(n^2)
S(n) : O(n)
"""


"""
Approach 2 : Sliding Window

 - intitate a variable maxLen = 0 - that will return the final ans
 - have two pointers - l =0
 - maintain a charset
 - run through all characters with r :
   - if the character at r in character set - keep removing the charcter at l and shrink the character set
     : since substring
   - increment l
   if char at r not in charset :
    - add the character in char set
    - max len is max of maxlen, curent diff in ptr + 1 (since strting from 0)
- return maxLen
"""

def lengthOfLongestSubstringSinglePass(s : str) -> int :
    maxLen = 0
    charSet = set()
    l = 0

    for r in range(len(s)) :
        while s[r] in charSet :
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        maxLen = max(maxLen, (r - l) + 1)
    return maxLen

s = "pwwkew"
ans = lengthOfLongestSubstringSinglePass(s)
print(ans)

"""
T(n) : O(n)
S(n) : O(n)

"""
