"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.


Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

"""

"""
Approach 1 : Sort and compare

-maintain ans =[]
 - for each str :
   currList = [str]
  - if sorted of currentStr is equal to str :
     - append it to currList
 - append currList to ans
- return ans

"""

from typing import List

def groupAnagrams(strs : List[str]) -> List[List[str]] :

    hmap = {}
    for string in strs :
        sortedString = "".join(sorted(string))

        if sortedString not in hmap :
            hmap[sortedString] = []
        hmap[sortedString].append(string)
    return list(hmap.values())


strs = ["eat","tea","tan","ate","nat","bat"]
ans = groupAnagrams(strs)
print(ans)



"""
T(n) : O(m * nlogn)
S(n) : O(n)
"""