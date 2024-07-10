"""
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

Input: nums = [3,0,1]
Output: 2

Input: nums = [0,1]
Output: 2

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
"""

"""
Approach 1: Sort and Search

-  first we sort the list
- check for 3 cases :
  - if first element is not 0 -> return 0
  - if last element is not n -> return n
  - else run a loop till n, return the number not equal to index
"""

from typing import List

def missingNumber(nums : List[int]) -> int :
    nums.sort()
    # Case 1 : 0 not present
    if nums[0] != 0 :
        return 0
    # Case 2 : last number is not present
    if nums[-1] != len(nums) :
        return len(nums)
    # Case 3 : middle number is not present
    for i in range(len(nums)) :
        if i != nums[i] or nums[i] == None :
            return i

nums = [0,1]
#ans = missingNumber(nums)
#print(ans)

"""
T(n) : O(nlogn)
S(n) : O(1)
"""

"""
Approach 2 : Search diff

- search for the diff between the len and element
- the miss number is the diff which is not present
"""

def missingNumberDiff(nums : List[int]) -> int :
    n = len(nums)
    totalSum = (n * (n+1)) // 2
    listSum = sum(nums)
    return totalSum - listSum

nums = [3,0,1]
ans = missingNumberDiff(nums)
print(ans)

"""
T(n) : O(n)
S(n) : O(1)
"""
