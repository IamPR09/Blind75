"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


"""

"""
Approach 1 : Looping

- for each element
  - compare with rest 
  - if matches -> return true
  - else return false
"""

from typing import List

def containsDuplicate_App1(nums : List[int]) -> bool :

    for i in range(len(nums) - 1) :
        for j in range(i+1, len(nums)) :
            if nums[i] == nums[j] :
                return True
    return False

nums = [1,2,3]
result = containsDuplicate_App1(nums)
#print(result)
        
"""

T(n) : O(n^2)
S(n) : O(1)

"""

"""
Approach 2 : Sort and sliding window

- sort the list
- compare each element with next
  - if same -> return True
  - else return False
"""

def containsDuplicate_App2(nums : list[int]) -> bool :
    nums.sort()
    for i in range(len(nums)-1) :
        if nums[i] == nums[i+1] :
            return True
    return False

nums = [1,2,3,1]
result = containsDuplicate_App2(nums)
#print(result)

"""
T(n) : O(nlogn)
S(n) : O(1)
"""

"""
Approach 3 : Single Pass - Hashmap

- for each element if it doesnt exist in hash map
 - add
 - else return True
- finally return False

"""

def containsDuplicate_App3(nums : List[int]) -> bool :
    hmap={}
    for i in range(len(nums)) :
        if nums[i] in hmap :
            return True
        else:
            hmap[nums[i]] = i
    return False

nums = []
result = containsDuplicate_App3(nums)
print(result)

"""
T(n) : O(n)
S(n) : O(n)
"""