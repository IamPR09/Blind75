""" 
Given an integer array nums and an integer k, return the kth largest element in the array. 
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting ?
"""


import heapq

def kthLargest(nums :list[int], k :int) -> int :

    maxheap=[]
    for num in nums:
        heapq.heappush(maxheap,-num)
        if len(maxheap) > k :
            heapq.heappop(maxheap)
    return -maxheap[0]
    
arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4
ans = kthLargest(arr,k)
print(ans)