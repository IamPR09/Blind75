"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
determine if a person could attend all meetings.

Input: intervals = [(0,30),(5,10),(15,20)]
Output: false

"""

"""
Approach : Sort and compare

 - Sort the intervals by their first element
 - for each interval starting from first :
    - compare if start < prev end
     - If no return False
      - else continue
 - in the end return True
"""

from typing import List


def attendMeetings(intervals : List[Interval]) :
    intervals.sort(key = lambda i : i.start)

    for i in range(1,len(intervals)) :
        if intervals[i].start < intervals[i-1].end :
            return False
    return True

intervals = [(0,30),(5,10),(15,20)]
print(attendMeetings(intervals))

"""
T(n) : O(nlogn)
S(n) : O(1)

"""