"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.


"""

"""
Approach 1 : Looping
- maintain maxArea
- for each element
 - maxwater is max between maxArea and product of min numbers and index diff
return maxArea


"""

from typing import List

def maxAreaLoop(height : List[int]) -> int :
    maxWater = 0
    for i in range(len(height) - 1) :
        for j in range(i+1, len(height)) :
            currentArea = min(height[i], height[j]) * (j-i)
            maxWater = max(maxWater, currentArea)

    return maxWater

height = [1,1]
# result = maxAreaLoop(height)
# print(result)

"""
T(n) : O(n^2)
S(n) :O(1)
"""

""""
Approach 2 : Single Pass - 2 pointer

- maintain maxWater = 0
- l,h at first and last element
 - compare and get max water which is max of maxwater and product of min value betweenl,h and diff of the l,h
 - if l<=h ->increment l
 - else decrement h
return maxWater
"""

def maxArea2Pointer(height : List[int]) -> int :
    maxArea = 0
    l,h = 0, len(height) - 1
    while l<h :
        currentMax = min(height[l], height[h]) * (h - l)
        maxArea = max(maxArea,currentMax)
        if height[l] < height[h] :
            l+=1
        else:
            h-=1
    return maxArea
        
height = [1,8,6,2,5,4,8,3,7]
result = maxArea2Pointer(height)
print(result)

"""
T(n) : O(n)
S(n) :O(1)
"""