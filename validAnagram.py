"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
"""


"""
Approach 1 :  Looping

- compare if length of two strings are same or not
 - if not return False
 - if yes
   - for each character in s, if we find that character in t -> replace it with "" and only 1 count
"""

def validAnagramLooping(s : str, t: str) -> bool :
    if len(s) != len(t) :
        return False
    for i in range(len(s)) :
        for j in range(len(t)) :
            if s[i] == t[j]:
                t = t.replace(t[j],"",1)
                break
    return t == ""

s = "ract"
t = "car"
# ans = validAnagramLooping(s,t)
# print(ans)

"""
T(n) : O(n^2)
S(n) : O(1)
"""

"""
Approach 2 : Sorting

- sort the two strings
- return if they are same
"""

def validAnagramSorting(s: str, t: str) -> bool :
    if len(s) != len(t) :
        return False
    s = sorted(s)
    t = sorted(t)
    return s == t

#ans = validAnagramSorting(s,t)
#print(ans)


"""
T(n) : O(nlogn)
S(n) : O(1)
"""

"""
Approach 3 :  Hash Map

- maintain a map of distinct chars in s
- maintain a map of distinct chars in t
- return if both dictionaries are same
"""

def validAnagramHash(s: str, t: str) -> bool :
    if len(s) != len(t):
        return False
    
    sDict = {}
    tDict = {}
    for chars in s :
        if chars not in sDict.keys() :
            sDict[chars] = 1
    for chart in t :
        if chart not in tDict.keys() :
            tDict[chart] = 1
    return sDict == tDict

ans = validAnagramHash(s,t)
print(ans)

"""
T(n) : O(n)
S(n) : O(n)
"""