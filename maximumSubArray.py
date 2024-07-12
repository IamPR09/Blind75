"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

"""


"""
Approach 1 : Looping

- set maxSum = first element 
-  for each element
 - consider all possible iterations and calculate sum
 - compapre the sum with maxSum and update if greater
- return maxSum
"""

from typing import List

def maxSubarray_Loop(nums : List[int]) -> int :
    maxSum = nums[0]
    for i in range(len(nums) - 1) :
        currentSum = nums[i]
        for j in range(i+1, len(nums)) :
            currentSum += nums[j]
            if currentSum > maxSum :
                maxSum = currentSum

    return maxSum

nums = [5,4,-1,7,8]
result = maxSubarray_Loop(nums)
# print(result)

"""
T(n) : O(n^2)
S(n) : O(1)

"""

"""
Approach 2 : Kadane's Algo (Discard if Sum < 0)

- for each element
 - maintain current sum
 - if current sum < 0
  - reset current sum to 0
  - else maintain max sum as max (max sum and current sum)
- return maxSum

"""

def maxSubArray_Kadane(nums : List[int]) -> int :
    maxSum = nums[0]
    currentSum = 0
    for ix,val in enumerate(nums) :
        currentSum += val

        maxSum = max(maxSum, currentSum)

        if currentSum < 0 :
            currentSum = 0
    return maxSum


nums = [-2,1,-3,4,-1,2,1,-5,4]
result = maxSubArray_Kadane(nums)
print(result)

"""
T(n) : O(n)
S(n) : O(1)
"""