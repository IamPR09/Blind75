"""
Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.

Input: nums = [2,3,2]
Output: 3

Input: nums = [1,2,3,1]
Output: 4

"""

"""
Approach 1 : extension of House Robber

 - for each position: maintian cases of maxRob if robbed prev, or 2 before
 - call this on 2 halves
   - one from 1 to second last index
   - one from 2 to last index
   - Any other Edge case ??
"""

from typing import List


def houseRobberII(nums : List[int]) -> int :

    def helper(nums : List[int]) -> int :
        robOneBefore = 0
        robTwoBefore = 0
        for num in nums :
            newRob = max(num + robTwoBefore, robOneBefore)
            robTwoBefore = robOneBefore
            robOneBefore = newRob
        return robOneBefore
    
    return max(nums[0], helper(nums[1:]), helper(nums[:-1]))


house = [1,2,3,1]
ans = houseRobberII(house)
print(ans)


"""
T(n) : O(n)
S(n) : O(1)

"""

