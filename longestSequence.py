"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Input: nums = [100,4,200,1,3,2]
Output: 4


"""


"""
Approach 1 : Sorting
- initiate a var maxLen
- sort the list
- for each element : 
  - currlen = 0
  - if next is + 1
     - currLen+1 
  - take max of maxLen, currLen 



 # sorted
 # [1,2,3,4,100,200] 

"""

from typing import List

def longestSequence(nums: List) -> int :
    nums.sort()
    maxlen=0
    lastSmallest=-1
    currLen=0
    if len(nums) == 1:
        return nums[0]
    
    for num in nums :
        if num == lastSmallest:
            continue
        elif num == lastSmallest+1:
            lastSmallest = num
            currLen+=1
        else:
            currLen=1
            lastSmallest = num
        maxlen = max(maxlen,currLen)
    return maxlen

nums = [0,3,7,2,5,8,4,6,0,1]
ans = longestSequence(nums)
#print(ans)

"""
T(n) : O(nlogn + n)
S(n) : O(1)
"""



"""
Approach 2 : set and search in set
"""

def longestSequenceSet(nums:List[int]) -> int :
    numset = set(nums)
    maxLen=0

    for num in nums :
        if num-1 not in numset:
            length=0
            while num+length in numset:
                length+=1
            maxLen=max(length,maxLen)
    return maxLen

nums = [100,4,200,1,3,2]
ans2 = longestSequenceSet(nums)
print(ans2)


"""
T(n) : O(n)
S(n) : O(n)

"""