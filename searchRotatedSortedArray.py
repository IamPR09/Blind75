"""
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Input: nums = [1], target = 0
Output: -1
"""

"""
Approach 1 : Single Pass and search

- Just loop over each element
- if element equals target -> return index of target
"""

from typing import List

def searchLoop(nums : List[int], target : int) -> int :
    for ix,val in enumerate(nums) :
        if val == target :
            return ix
    return -1

nums = [4, 5,6,7,0,1,2]
target = 3
# res = searchLoop(nums,target)
# print(res)

"""
S(n) : O(n)
T(n) : O(1)

"""

"""
Approach 2 : Sort (Binary search)

- maintain l,r,m
- compare target with m
 - if target is less than m
  - compare target with l
  - if less : -> make l = mid+1
  - else case -> make r = mid -1
 - else compare target with r
  - if more: -> r = mid - 1  
  - else l = mid + 1

"""

def searchBin( nums : List[int], target : int) -> int :
    l = 0
    r = len(nums) - 1
    while l <= r :
        mid = (l + r) // 2
        if nums[mid] == target :
            return mid
        if nums[l] <= nums[mid] :
            if target > nums[mid] or target < nums[l] :
                l = mid + 1
            else :
                r = mid - 1
        else :
            if target < nums[mid] or target > nums[r] :
                r = mid - 1
            else :
                l = mid + 1
    return -1

        
nums = [4, 5,6,7,0,1,2]
target = 0
res = searchBin(nums,target)
print(res)

"""
T(n) : O(log n)
S(n) : O(1)
"""
