"""
Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers,
return the number with the largest value.

Example 1:

Input: nums = [-4,-2,1,4,8]
Output: 1

Input: nums = [2,-1,1]
Output: 1


"""


from typing import List


def findClosest(nums : List[int]) -> int :
    ans = -float("inf")
    min_dist = float("inf")

    for num in nums :
        curr_dist = abs(num - 0)
        if curr_dist < min_dist :
            min_dist = curr_dist
            ans = num
        if curr_dist == min_dist:
            if num > ans :
                ans = num
    return ans

nums = [2,1,-1]
output = findClosest(nums)
print(output)


"""
T(n) -> O(n)
S(n) -> O(1)
"""