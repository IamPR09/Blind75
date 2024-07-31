"""
Given an integer array nums and an integer k, return the k most frequent elements.
 You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

"""

"""
Approach 1 : Max Heap - K pops

T(n) : klogn
"""


"""
Approach 2 : counter map and Sort


- create a map
- for each element in nums :
  - maintain a count map
- sort the count map by counts (values)
- add the values in resList until len is k 
"""

from typing import List


def topKFreq(nums : List[int], k : int) -> List[int] :
    countMap = {}
    for num in nums :
        if num not in countMap :
            countMap[num] = 1
        else :
            countMap[num] += 1
    countMap = {key:v for key, v in sorted(countMap.items(), key = lambda x : x[1], reverse = True)}

    resList = []
    for key,v in countMap.items():
        resList.append(key)
        if len(resList) == k:
            return resList

nums = [1,1,1,2,2,3]
k = 2
ans = topKFreq(nums, k)
print(ans)



"""
T(n) : O(nlogn)
S(n) : O(n)
"""