"""
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals
 you need to remove to make the rest of the intervals non-overlapping.


Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1

"""

"""
Approach 1 - Sort and Count


- sort the intervals by their first value
- maintain last end
- compare it with rest
  - if current start is more or equal to prev end : definitely the end is more than prev end
    - update last end to be current end
  - increment by 1
  - new last end = minimum of current end or last end
- 
      
"""

from typing import List

def eraseOverlap(intervals : List[List[int]]) -> int :
    intervals.sort(key = lambda i : i[0])
    res = 0
    prevEnd = intervals[0][1]
    for start,end in intervals[1:] :
        if start >= prevEnd :
            prevEnd = end
        else :
            res+=1
            prevEnd = min(end,prevEnd)

    return res

intervals = [[1,2],[2,3],[3,4],[1,3]]
ans = eraseOverlap(intervals)
print(ans)
    
"""
T(n) : O(nlogn)
S(n) : O(n)
"""
   