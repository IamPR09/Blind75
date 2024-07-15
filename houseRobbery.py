"""
Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

Input: nums = [1,2,3,1]
Output: 4

Input: nums = [2,7,9,3,1]
Output: 12

"""

from typing import List

def houseRobber(nums : List[int]) -> int :
    robOneBefore = 0
    robTwoBefore = 0
    for n in nums :
        temp = max(n + robTwoBefore, robOneBefore)
        robTwoBefore = robOneBefore
        robOneBefore = temp
    return robOneBefore

nums = [2,7,9,3,1]
ans = houseRobber(nums)
print(ans)


"""
T(n) : O(n)
S(n) : O(1)
"""