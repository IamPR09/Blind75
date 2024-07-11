"""
Given an integer array nums, find a subarray that has the largest product, and return the product.
Example 1:

Input: nums = [2,3,-2,4]
Output: 6

Input: nums = [-2,0,-1]
Output: 0

"""

"""
Approach 1 : Looping

"""



from typing import List

def maxProductLoop(nums : List[int]) -> int :
    maxProduct = max(nums) 
    for i in range(len(nums) - 1) :
        candP = nums[i]
        for j in range(i+1, len(nums)) :
            candP *= nums[j]
            maxProduct = max(maxProduct,candP)
    return maxProduct

nums = [-2,0,-1]
# ans = maxProductLoop(nums)
# print(ans)

"""
T(n) : O(n^2)
S(n) : O(1)
"""



"""
Approach 2 : max, min maintenance

"""

def maxProdOptimal(nums : List[int]) -> int :
    maxProd = max(nums)
    currMax, currMin = 1, 1
    for num in nums :
        candP = currMax * num
        currMax = max(candP, currMin * num, num)
        currMin = min(candP, currMin * num, num)
        maxProd = max(maxProd,currMax)
    return maxProd

nums = [2,3,-2,4]
ans = maxProdOptimal(nums)
print(ans)


"""
T(n) : O(n)
S(n) : O(1)
"""