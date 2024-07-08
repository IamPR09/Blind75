"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.


"""

"""
Approach 1 : 2 pointer compare
- for each element
 - compare each one with the next
  - if next element is smaller than the current element -> return the next element
 
Since its a sorted array we know that there will be a smaller element
"""

from typing import List

def findMinTwoPointer(nums : List[int]) -> int :
    for i in range(len(nums) - 1) :
        if nums[i] > nums[i+1] :
            print("Array is rotated {} times".format(i+1))
            return nums[i+1]
    print("The array was rotated {} times".format(len(nums)))
    return nums[0]

nums = [3,4,5,1,2]
#res = findMinTwoPointer(nums)
#print(res)

"""
T(n) : O(n)
S(n) : O(1)
"""

"""
Approach 2 : Sorting (Log n)

- sort the list 
 - return the first element
"""

def findMinSorted(nums : List[int]) -> int :
    nums.sort()
    return nums[0]

# resultSorted = findMinSorted(nums)
# print(resultSorted)

"""
T(n) : O(log n)
S(n) :O(1)
"""

"""
Approach 3: Implement sorting - Binary Sort

- set res = first element
- set l,r to first and last element
- if l < r -> already sorted
 - return min (res, value at l) 
 - break
- set middle element as l+r//2
 - compare if value at mid is less than value at l
  - if yes : search in right portion : l = mid + 1
  - else : r = mid-1
return res


"""

def findMinBinarySearch(nums : List[int]) -> int :
    res = nums[0]
    l,r = 0, len(nums) - 1
    while l <=r :
        if nums[l] < nums[r] :
            return min(res,nums[l])
        mid = (l + r) // 2
        if nums[mid] > nums[l] :
            l = mid + 1
        else :
            r = mid - 1
    return res

resultbinSearch = findMinBinarySearch(nums)
print(resultbinSearch)


"""
T(n) : O(log n)
S(n) : O(1)
"""

            
