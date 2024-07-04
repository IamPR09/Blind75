

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


Input: nums = [3,2,4], target = 6
Output: [1,2]

"""


"""
Approach 1 : Looping

 - for each number, compare with the rest of the numbers
 - if the sum of two numbers equal target --> return their indices

"""
from typing import List


def twoSum_App_1(nums: List[int], target : int) -> List[int]:
    reuslt_indices=[]

    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target :
                reuslt_indices.append(i)
                reuslt_indices.append(j)
    
    return reuslt_indices

nums = [2,7,11,15]
target = 9

nums = [3,2,4]
target = 6

nums = [3,3]
target = 6

nums = [1,2,3,9,5,6,15,25]
target = 26

result = twoSum_App_1(nums,target)
print(result)


"""
T(n) : O(n^2)
S(n) : O(1)

"""




"""
Approach 2 : Single pass (Hash map)

 - maintain a map of nums : index
 - loop over each element within the list
    - search for target-nums in map keys
    - if exist, return current index and value of map[target-element]

"""

def twoSum_App_2(nums : List[int], target : int) -> List[int]:
    hmap={}
    for i in range(len(nums)):
        if target - nums[i] in hmap:
            return [i,hmap[target - nums[i]]]
        else:
            hmap[nums[i]] = i
        
nums = [2,7,11,15]
target = 9

nums = [1,2,3,9,5,6,15,25]
target = 26

result = twoSum_App_2(nums,target)
print(result)

"""
T(n) : O(n)
S(n) : O(n)

"""

