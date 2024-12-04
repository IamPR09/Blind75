"""
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

"""

"""
Approach :
 - Use map and Priority queue
 - maintain count of nums in map
  - k:v -> num : count(num)
- use priority queue (max heap) -> based on count
- take max till k and return the key of max val from map

"""
from collections import Counter
from typing import List
import heapq

def topKFrequent(nums : List[int], k:int) -> List[int]:
    countMap = Counter(nums)
    countMapDesc = dict(sorted(countMap.items(), key=lambda item : item[1], reverse=True))

    minHeap=[]
    for num,count in countMapDesc.items():
        heapq.heappush(minHeap,(count,num))
        if len(minHeap) > k:
            heapq.heappop(minHeap)
    return [pair[1] for pair in minHeap]
    



    # {1:3, 2:2, 3:1}
    
nums = [1,1,1,2,2,3]
k = 2  

ans = topKFrequent(nums,k)
print(ans)

