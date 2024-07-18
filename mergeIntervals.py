"""
Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals
in the input.

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

"""

"""
Approach 1 : Sorting

- Sort by the first element
- append the first interval in output
- for each interval
  - compare the start element with the end element of last appended interval
      - if small : append last element of appended interval as max (end of last appended vs current end)
 - append the interval
"""

from typing import List

def merge(intervals : List[List[int]]) -> List[List[int]] :
    intervals.sort(key = lambda i : i[0])
    output = [intervals[0]]

    for start,end in intervals[1:]:
        if start <= output[-1][1] :
            newEnd = max(end, output[-1][1])
            output[-1][1] = newEnd
        else :
            output.append([start,end])

    return output


intervals = [[1,4],[4,5]]
mergedInterval = merge(intervals)
print("merged intervals are {}".format(mergedInterval))


"""
S(n) : O(nlogn)
T(n) : O(n)
"""