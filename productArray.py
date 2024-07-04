"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

"""

"""
Approach 1 : Looping

- for each element:
 - run a loop again and check if indexes are not same and number at index is > 0:
 - store the product at that index at end of second loop
"""

from typing import List

def productArrayLoop(nums : List[int]) -> List[int] :

    result=[]
    for i in range(len(nums)) :
        prod = 1
        for j in range(len(nums)) :
            if j!=i :
                prod = prod * nums[j]
            
        result.append(prod)
        
    return result

nums = [1,2,3,4]
# nums = [-1,1,0,-3,3]
#res = productArrayLoop(nums)
#print(res)

"""
T(n) : O(n^2)
S(n) : O(n)
"""

"""
Approach 2 : forward and reverse product

- till each index maintain 2 values
 - forward prod -> product of all numbers before that index (excluded)
 - reverse product -> product of all numbers after that (excluded)
- value at each index is a product of forward prod and reverse prod
"""

def productArrayForwardbackward(nums : List[int]) -> List[int] :
    result = []
    forwardProd,backwardProd = [],[]
    fp = 1
    for i in range(len(nums)) :
        if i !=0 :
            fp = fp * nums[i-1]    
        forwardProd.insert(i,fp)
    print("FP", forwardProd)
    
    # forwardProd = [1,1,2,6]
    bp = 1
    for j in range(len(nums)-1,-1,-1) :
    
        if j != len(nums) - 1 :
            bp = bp * nums[j+1]
        backwardProd.append(bp)
        
    backwardProd.reverse()
    print("BP",backwardProd)

    #backwardProd = [24,12,4,1]

    for k in range(len(nums)):
        result.insert(k, (forwardProd[k] * backwardProd[k]))
    return result

nums = [-1,1,0,-3,3]
res = productArrayForwardbackward(nums)
print(res)

"""
T(n) : O(n)
S(n) : O(n)
"""




